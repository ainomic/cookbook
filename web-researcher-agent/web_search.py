from langchain.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults
from langchain.utilities import DuckDuckGoSearchAPIWrapper

search = DuckDuckGoSearchRun()
print(search.run("What is the capital of France?"))

print("-----")
search = DuckDuckGoSearchResults()
print(search.run("What is the capital of France?"))

print("-----")
wrapper = DuckDuckGoSearchAPIWrapper(region="en-IN", time="d", max_results=2)
search = DuckDuckGoSearchResults(api_wrapper=wrapper)
print(search.run("What is the capital of France?"))
