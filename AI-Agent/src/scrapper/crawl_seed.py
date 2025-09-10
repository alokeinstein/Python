# Step 3: Create crawl_seed.py
# Create the script in src/scraper--->touch src/scraper/crawl_seed.py
# Open in editor: code src/scraper/crawl_seed.py
# Inside: Use if __name__ == "__main__":
# - Take args: sitemap_url (required), N (optional, default 5 for first N pages).
# - Use argparse for better CLI (import argparse).
# - Call parse_sitemap to get URL list.
# - For each of first N URLs: Run the scraping logic (import and call from simple_scraper.py, or reuse code).
# - For each scraped dict: Extract domain from URL (use urllib.parse.urlparse).
# - Create dir: mkdir -p data/raw/<domain>
# - Save as JSON: Use json.dump to file like data/raw/<domain>/<slug_or_id>.json (make filename from URL path).
# - Handle errors gracefully (e.g., skip bad URLs).

import requests 
from bs4 import BeautifulSoup
import sitemap


result = sitemap.parse_sitemap("https://www.codersdaddy.com/sitemap.xml")
n_url = result[1:2]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
response = requests.get(n_url,headers=headers)
print(response)
# soup = BeautifulSoup(response.text, 'html.parser')
# # h2_heading = [for heading in soup.find_all("h2") h2_heading.append(heading.text)]
# h2_heading = [heading.text for heading in soup.find_all("h2")]
# print(h2_heading)
