# Open in editor: code src/scraper/sitemap.py (or your editor command)
# Inside: Define a function parse_sitemap(sitemap_url) that:
# - Fetches the sitemap XML using requests (with User-Agent).
# - Parses XML with BeautifulSoup (use 'xml' parser).
# - Extracts <loc> tags for URLs (handle nested sitemaps if needed, but keep simple for now).
# - Returns a list of URLs.


# bs4: Beautiful Soup is a Python library for pulling data out of HTML and XML files.
# lxml: It is a Python library that allows us to handle XML and HTML files.


import requests
from bs4 import BeautifulSoup 

def parse_sitemap(sitemap_url):
     sitemap_url = sitemap_url.strip()
     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
     
     try:
        response = requests.get(sitemap_url, headers= headers)
        response.raise_for_status()
     except Exception as e:
        print(f"Failed to fetch: {e}")
        return []
        
     soup = BeautifulSoup(response.content, 'xml')
     # print(soup)
     loc_tag = soup.find_all('loc')
     urls = [tag.get_text().strip() for tag in loc_tag]
     return urls
     

"""This line calls the function but does not print the urls in the console, so other ways can be, you can return a print() or use use function copy method and print the copied function. """
# parse_sitemap("https://www.codersdaddy.com/sitemap.xml")
result = parse_sitemap("https://www.codersdaddy.com/sitemap.xml")
print(result)

##NEW THINGS I LEARNT
"""
1. <loc> tag is not present in the HTML file , it is only present in XML file.
2. normal url like "https://www.codersdaddy.com" will not give you xml file 
3. even if you try to extract the content from the xml parser. You have to give me sitemap.xml url 

4. 📌 Exception: A malicious or misconfigured site could put a <loc> tag in HTML — but it’s meaningless there and not standard.
"""
