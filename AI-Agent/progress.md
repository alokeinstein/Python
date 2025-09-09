Day 1:
--> Create the directory structure: mkdir -p src/scraper.
-->Inside src/scraper, create simple_scraper.py.
-->Open the file in your editor and build it step by step:

-->Import statements: At the top, import requests, bs4.BeautifulSoup, urllib.parse (for URL handling), and json (for output).
-->Define the main function or script body: Use if __name__ == "__main__": to wrap the logic.

-->Take a URL as a command-line argument (use sys.argv[1] or argparse for better UX; start simple with sys).
-->Set up a User-Agent header to mimic a browser (e.g., a string like 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...' – copy a real one from your browser dev tools).
-->Make a GET request to the URL with requests.get(url, headers={'User-Agent': user_agent}). Handle basic errors (e.g., check response.status_code == 200).
-->Parse the response content: soup = BeautifulSoup(response.text, 'html.parser').
Extract elements:

-->Title: soup.find('title').text.strip() if exists, else empty string.
Meta description: soup.find('meta', attrs={'name': 'description'})['content'].strip() if found.
-->H1: soup.find('h1').text.strip() if exists.
-->H2s: [h.text.strip() for h in soup.find_all('h2')].
-->Canonical link: soup.find('link', attrs={'rel': 'canonical'})['href'] if found; make it absolute using urllib.parse.urljoin(url, href).
-->All links: [urllib.parse.urljoin(url, a['href']) for a in soup.find_all('a', href=True)] (filter out None or empty).
-->Article text (best-effort): Try selectors like soup.find('article'), or .content, or .post. -->If found, extract text with .get_text(separator=' ', strip=True) or recursively from paragraphs ([p.text.strip() for p in container.find_all('p')]). Join into a single string; if none, use the full soup.get_text().


-->Store everything in a Python dict (e.g., {'title': title, 'description': desc, ...}).
Print the JSON: print(json.dumps(data, indent=2, ensure_ascii=False)).




-->Test it manually: Run python src/scraper/simple_scraper.py https://example.com (use a real news site like a BBC article for better testing). Check the output JSON for the extracted fields.

Step 4: Create the README