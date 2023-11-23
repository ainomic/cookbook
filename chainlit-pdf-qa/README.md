# Chat with your data

Upload your document and chat w/ your data.

## How it works?

- User uploads a document (pdf, txt, etc.)
- Chunk the document and create embeddings
- Store these embeddings into Pinecone vector DB
- User can ask questions over this document
- App takes the question and find relevant information from the document
- LLM synthesize this information to respond back to the user.

## Run the application

1. Create virtual environment: `conda create -n chainlit-pdf-qa-env -y python=3.10`
1. Activate virtual environment: `conda activate chainlit-pdf-qa-env`
1. Install dependencies: `pip install -r requirements.txt`
1. Run: `chainlit run app.py -w`
1. Browse [here](http://localhost:8000/)
1. Upload sample document from [state_of_the_union.txt](data/state_of_the_union.txt)
1. Ask questions like:
   - What is this file about?
   - Who rejected repeated efforts at diplomacy?
   - How many members were present in European Union?
