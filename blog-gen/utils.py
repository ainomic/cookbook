import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.chains import ReduceDocumentsChain, MapReduceDocumentsChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
import time


def save_uploaded_file(file):
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    return file_path


def process_uploaded_file(file_path):
    docs = PyPDFLoader(file_path).load()
    print(len(docs))

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024, chunk_overlap=10,
    )
    split_docs = text_splitter.split_documents(docs)
    print("Split docs:", len(split_docs))
    return split_docs


def build_llm(api_key=None):
    return ChatOpenAI(model="gpt-4",
                      temperature=0,
                      openai_api_key=api_key or os.getenv("OPENAI_API_KEY"))


def build_map_chain(llm):
    map_template = """The following is a set of documents:
---
{docs}
---
Based on these documents, summarise them to help writing a detailed Medium blog article.
Summary:"""
    map_prompt = PromptTemplate.from_template(map_template)
    map_chain = LLMChain(llm=llm, prompt=map_prompt)
    return map_chain


def build_reduce_chain(llm):
    # Reduce
    reduce_template = """The following is a set of summaries:
---
{doc_summaries}
---
Take these and distill it into a final, consolidated summary of the content to help writing a detailed Medium blog article.
Summary:"""
    reduce_prompt = PromptTemplate.from_template(reduce_template)
    # Run chain
    reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)

    # Takes a list of documents, combines them into a single string, and passes this to an LLMChain
    combine_documents_chain = StuffDocumentsChain(
        llm_chain=reduce_chain, document_variable_name="doc_summaries"
    )

    # Combines and iteravely reduces the mapped documents
    reduce_documents_chain = ReduceDocumentsChain(
        # This is final chain that is called.
        combine_documents_chain=combine_documents_chain,
        # If documents exceed context for `StuffDocumentsChain`
        collapse_documents_chain=combine_documents_chain,
        # The maximum number of tokens to group documents into.
        token_max=4000,
    )
    return reduce_documents_chain


def build_map_reduce_chain(llm):
    map_chain = build_map_chain(llm)
    reduce_documents_chain = build_reduce_chain(llm)
    # Combining documents by mapping a chain over them, then combining results
    map_reduce_chain = MapReduceDocumentsChain(
        # Map chain
        llm_chain=map_chain,
        # Reduce chain
        reduce_documents_chain=reduce_documents_chain,
        # The variable name in the llm_chain to put the documents in
        document_variable_name="docs",
        # Return the results of the map steps in the output
        return_intermediate_steps=False,
    )
    return map_reduce_chain


def build_blog_chain(llm):
    prompt_template = """Based on the following context:
---
{context}
---
Please generate a detailed Medium blog article and strictly output in a Markdown text. Keep the article interesting to read and divide it into multiple sections as applicable.
Do not include any image, hyperlink in the generated article, and not make any reference to these documents in the generated article such as "In a set of documents", "the documents", etc.
Article:"""
    llm_chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate.from_template(prompt_template)
    )
    return llm_chain


def generate(split_docs, api_key=None):
    llm = build_llm(api_key)

    map_reduce_chain = build_map_reduce_chain(llm)
    print(f"Running MapReduce chain...")
    start = time.time()
    result = map_reduce_chain.run(split_docs)
    print(f"MapReduce chain completed in {time.time() - start}s")

    blog_chain = build_blog_chain(llm)
    print(f"Running Blog chain...")
    start = time.time()
    blog_result = blog_chain.run(context=result)
    print(f"Blog chain completed in {time.time() - start}s")
    return blog_result
