from langchain.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults
from langchain.utilities import DuckDuckGoSearchAPIWrapper
import requests
from bs4 import BeautifulSoup


RESULTS_PER_QUESTION = 3
ddg_search = DuckDuckGoSearchAPIWrapper()


def scrape_text(url: str):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            page_text = soup.get_text(separator=" ", strip=True)

            return page_text
        else:
            return f"Failed to retrieve the webpage: status code {response.status_code}"
    except Exception as e:
        print(e)
        return f"Failed to retrieve the webpage: {e}"


def web_search(query: str, num_results: int):
    results = ddg_search.results(query, num_results)
    return [r["link"] for r in results]


def get_links(query: str):
    return [{
        "url": url,
        "question": query,
    } for url in web_search(query, RESULTS_PER_QUESTION)]


if __name__ == "__main__":
    query = "What is the capital of France?"
    links = web_search(query, RESULTS_PER_QUESTION)
    scraped_data = []
    for link in links:
        scraped_text = scrape_text(link)
        scraped_data.append(scraped_text)
