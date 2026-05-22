import sys
import requests
from crawl import extract_page_data

def get_html(url):
    try:
        response = requests.get(url, headers={"User-Agent": "BootCrawler/1.0"})
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

def crawl_page(base_url, current_url=None, page_data=None):
    if current_url is None:
        current_url = base_url
    if page_data is None:
        page_data = {}

    html = get_html(current_url)
    if not html:
        return

    data = extract_page_data(html, current_url)
    page_data[current_url] = data

    for link in data["outgoing_links"]:
        if link.startswith(base_url) and link not in page_data:
            crawl_page(base_url, link, page_data)
    
    return page_data

def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)
    print("starting crawl of:", sys.argv[1]) # BASE_URL
    page_data = crawl_page(sys.argv[1])
    # Print total pages crawled and some sample data
    print(f"Total pages crawled: {len(page_data)}")
    print("Sample page data: ", next(iter(page_data.values())))
    print("crawl complete")



if __name__ == "__main__":
    main()
