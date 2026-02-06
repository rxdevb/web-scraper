import requests
from bs4 import BeautifulSoup

def run_scraper():
    print("Starting scraper...")
    url = "https://news.ycombinator.com/"
    print(f"Fetching {url}")
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        page_title = soup.title.string
        print(f"Page title: {page_title}")

        print("\n 5 lasts news:")
        news_items = soup.find_all(class_="titleline", limit=5)

        for idx, item in enumerate(news_items, 1):
            link = item.find('a')
            print(f"{idx}. {link.get_text()} -> {link['href']}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_scraper()        
