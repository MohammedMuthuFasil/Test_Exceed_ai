import requests
from concurrent.futures import ThreadPoolExecutor
from urllib.robotparser
from urllib.parse import urljoin,urlparse

def is_allowed(url,user_agent="*"):
    parse_url = urlparse(url)
    base_url = f'{parse_url.scheme}://{parse_url.netloc}'
    robots_url = urljoin(base_url,'/robots.txt')
    
    rb  = urllib.robotparser.RobotFileParser()
    rb.set_url(robots_url)
    rb.read()
    return rb.can_fetch(user_agent, url)

def fetch_page(url):
    if not is_allowed(url):
        print(f"scrapping not allowed this {url}")
        return None
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully fetched {url}")
            return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None

def main():
    start_url = "htttp://example.com"
    page = fetch_page(start_url)
    if not page:
        return 
    
if __name__ == "__main__":
    main()