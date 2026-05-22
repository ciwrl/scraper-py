import urllib.parse

def normalize_url(url: str) -> str:
    parse_url = urllib.parse.urlparse(url)
    url = parse_url.netloc + parse_url.path
    # Convert to lowercase
    url = url.lower()
    return url