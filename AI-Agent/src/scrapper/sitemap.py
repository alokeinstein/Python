# Open in editor: code src/scraper/sitemap.py (or your editor command)
# Inside: Define a function parse_sitemap(sitemap_url) that:
# - Fetches the sitemap XML using requests (with User-Agent).
# - Parses XML with BeautifulSoup (use 'xml' parser).
# - Extracts <loc> tags for URLs (handle nested sitemaps if needed, but keep simple for now).
# - Returns a list of URLs.

import requests
from bs4 import BeautifulSoup

def parse_sitemap(sitemap_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(sitemap_url, headers= headers)