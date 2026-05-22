import urllib.parse
from bs4 import BeautifulSoup, Tag

def normalize_url(url: str) -> str:
    parse_url = urllib.parse.urlparse(url)
    url = parse_url.netloc + parse_url.path
    # Convert to lowercase
    url = url.lower()
    return url

def get_heading_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    h_tag = soup.find("h1")
    return h_tag.get_text(strip=True) if isinstance(h_tag, Tag) else ""

def get_first_paragraph_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    main_tag = soup.find("main")
    if main_tag:
        p_tag = main_tag.find("p")
        if p_tag:
            return p_tag.get_text(strip=True) if isinstance(p_tag, Tag) else ""
    p_tag = soup.find("p")
    return p_tag.get_text(strip=True) if isinstance(p_tag, Tag) else ""