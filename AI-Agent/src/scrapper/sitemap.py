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














#######################################################
# 🧠 MY WEB SCRAPING & SITEMAP NOTES — COPY & PASTE 🧠
#######################################################

✅ COVERED BY ME:
-------------------------------------------------------
1️⃣ <loc> TAGS ONLY EXIST IN XML SITEMAPS — NOT IN HTML PAGES.
   → Example: https://example.com/sitemap.xml ✅
   → Not in: https://example.com/ ❌

2️⃣ NORMAL WEB PAGES (like CNN or CodersDaddy homepage) RETURN HTML.
   → They contain <div>, <h1>, <p> — NOT <loc> tags.

3️⃣ TO GET <loc> TAGS → YOU MUST REQUEST A REAL SITEMAP.XML URL.
   → Always verify by opening the URL in browser first!

4️⃣ CODERSDADDY’S “sitemap.xml” IS NOT STANDARD XML — IT’S PLAIN TEXT!
   → No <loc> tags → soup.find_all('loc') returns [] ❌
   → Must parse line-by-line → if line.startswith('http') ✅

5️⃣ ALWAYS STRIP WHITESPACE FROM URLS → .strip() is your friend!
   → "url  " → breaks everything 😅

6️⃣ return print(urls) → RETURNS None ❌
   → Do: print(urls) THEN return urls ✅

7️⃣ XML PARSER WON’T CREATE <loc> TAGS IF THEY DON’T EXIST.
   → Garbage in → garbage out. Always check raw content first!

❗ WHAT I MISSED / SHOULD ADD:
-------------------------------------------------------
🔹 NOT ALL “sitemap.xml” FILES ARE THE SAME:
   - ✅ Standard XML (with <url><loc>...</loc></url>)
   - ⚠️ Plain Text (CodersDaddy style — raw URLs)
   - 🔄 Sitemap Index (contains <sitemap><loc>...</loc></sitemap> → points to child sitemaps)

🔹 ALWAYS CHECK Content-Type HEADER or RAW TEXT FIRST:
   → print(response.text[:500]) — see what you’re REALLY getting!

🔹 NAMESPACE AWARENESS (for strict XML sitemaps):
   → Some sitemaps use xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
   → BeautifulSoup sometimes needs help → but often .find_all('loc') still works!

🔹 ROBOTS.TXT IS YOUR BEST FRIEND:
   → https://example.com/robots.txt → look for Sitemap: ... 🗺️
   → Often reveals the TRUE sitemap URL!

🔹 ERROR HANDLING IS KEY:
   → Always wrap requests in try/except
   → Always check response.status_code
   → Use response.raise_for_status()

🔹 UNIVERSAL PARSER IDEA (BONUS):
   → Try XML → if no <loc> tags → fallback to text parsing → profit! 💰

💡 PRO TIPS I LEARNED:
-------------------------------------------------------
✨ ALWAYS INSPECT RAW CONTENT FIRST → Ctrl+U or print(response.text)
✨ USE .strip() ON URLS → avoid sneaky whitespace bugs 🐛
✨ return AND print SEPARATELY → don’t mix them!
✨ TEST WITH print() INSIDE FUNCTION → then return the actual data
✨ CODERSDADDY TAUGHT ME: Real-world sitemaps are messy — adapt your parser!

🚀 NEXT STEPS:
-------------------------------------------------------
→ Build a universal sitemap parser (XML + text + index)
→ Save URLs to CSV/JSON
→ Crawl extracted URLs for content
→ Add concurrency (async/threads) for speed
→ Respect robots.txt + add delays (be ethical scraper!)

📚 RESOURCES:
-------------------------------------------------------
- Sitemap Protocol: https://www.sitemaps.org/protocol.html
- robots.txt Spec: https://developers.google.com/search/docs/crawling-indexing/robots/intro
- BeautifulSoup Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

✅ YOU’RE DOING AWESOME — KEEP EXPERIMENTING!