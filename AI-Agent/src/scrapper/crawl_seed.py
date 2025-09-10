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
"""
import requests 
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import sitemap
import json

result = sitemap.parse_sitemap("https://www.codersdaddy.com/sitemap.xml")

#n_url is an array containing one element, so i am accessing one element
n_url = result[1:2][0]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
      response = requests.get(n_url,headers=headers)
      response.raise_for_status()
except Exception as e:
      print(f"Failed to fetch: {e}")
soup = BeautifulSoup(response.text, 'html.parser')

# h2_heading = [for heading in soup.find_all("h2") h2_heading.append(heading.text)]
h2_heading = [heading.text for heading in soup.find_all("h2")]
# print(h2_heading[0:2])

title_tag = soup.find("title")
title = title_tag.text.strip() if title_tag else "No Title Found"

description_tag = soup.find('meta', attrs={"name":"keywords"})
keywords_content = description_tag['content'].strip()


website_details = {
  "domain_name": urlparse(n_url).netloc,
  "h2 heading": h2_heading[0:3],
  "keyword_description": keywords_content,
  "title": title
}

with open('sitemapJSON.json','w', encoding='utf-8') as f:
    json.dump(website_details,f,indent=2)
    
    
"""



















#!/usr/bin/env python3
"""
crawl_seed.py - CLI tool to scrape first N URLs from a sitemap.

Usage:
    python crawl_seed.py https://example.com/sitemap.xml --n 5
"""

import argparse
import json
import os
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import sitemap  # Your custom sitemap parser module

# -------------------------------
# Helper: Clean path for filename
# -------------------------------
def path_to_filename(path):
    if not path or path == '/':
        return 'index'
    clean = path.strip('/').replace('/', '_')
    # Remove or replace unsafe characters
    clean = clean.replace(' ', '_').replace(':', '_').replace('?', '_').replace('&', '_')
    return clean or 'index'

# -------------------------------
# Helper: Scrape a single URL
# -------------------------------
def scrape_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        print(f"→ Fetching: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"⚠️  Failed to fetch {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract H2s
    h2_heading = [heading.get_text(strip=True) for heading in soup.find_all("h2")]

    # Extract title
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else "No Title Found"

    # Extract keywords meta tag
    description_tag = soup.find('meta', attrs={"name": "keywords"})
    keywords_content = description_tag['content'].strip() if description_tag and description_tag.get('content') else "No Keywords Found"

    # Build result dict
    parsed = urlparse(url)
    domain = parsed.netloc.split(':')[0]  # Remove port if any

    return {
        "url": url,
        "domain": domain,
        "h2_headings": h2_heading[:3],  # First 3 H2s
        "keyword_description": keywords_content,
        "title": title
    }

# -------------------------------
# Main Script
# -------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape first N URLs from a sitemap.")
    parser.add_argument("sitemap_url", help="URL of the sitemap.xml")
    parser.add_argument("-n", "--num", type=int, default=5, help="Number of URLs to scrape (default: 5)")

    args = parser.parse_args()

    print(f"📥 Parsing sitemap: {args.sitemap_url}")
    try:
        urls = sitemap.parse_sitemap(args.sitemap_url)
    except Exception as e:
        print(f"❌ Failed to parse sitemap: {e}")
        exit(1)

    if not urls:
        print("❌ No URLs found in sitemap.")
        exit(1)

    print(f"📋 Found {len(urls)} URLs. Processing first {args.num}...")

    # Take first N URLs
    target_urls = urls[:args.num]

    # Process each URL
    for i, url in enumerate(target_urls, 1):
        print(f"\n--- [{i}/{len(target_urls)}] ---")

        scraped_data = scrape_url(url)
        if not scraped_data:
            print("⏩ Skipping due to error.")
            continue

        # Create directory: data/raw/<domain>
        domain = scraped_data["domain"]
        dir_path = os.path.join("data", "raw", domain)
        os.makedirs(dir_path, exist_ok=True)

        # Generate filename from URL path
        parsed = urlparse(url)
        filename = path_to_filename(parsed.path) + ".json"
        file_path = os.path.join(dir_path, filename)

        # Save JSON
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(scraped_data, f, indent=2, ensure_ascii=False)
            print(f"✅ Saved: {file_path}")
        except Exception as e:
            print(f"❌ Failed to save {file_path}: {e}")

    print("\n🎉 Done!")
    
    
    
    
    
    """
    To run the code come in the folder wehre this file is:
    python crawl_seed.py https://www.codersdaddy.com/sitemap.xml --n 5
    
    and you will get the output in the terminal and files will be created
    """