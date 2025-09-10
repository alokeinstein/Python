import requests 
# bs4 is the module and BeautifulSoup is the class in it
from bs4 import BeautifulSoup

#get request is sent to the url from the requests library and we get the response
url = "https://www.codersdaddy.com"
response = requests.get(url)
# print(response.text)


#html.parser is built in parser of python so we dont need to import it.
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())# it print the html code in a structured format

headings = []
all_headings = soup.find_all("h2")
print(all_headings)

for heading in all_headings:
    headings.append(heading.text)

# print(headings)

title_tag = soup.find("title")
title = title_tag.text.strip() if title_tag else ""
# print(title)


# if i dont know the meta tag so i will find all the meta tags and then find the one i want
""" for meta in soup.find_all('meta', attrs={'name': True}):
        print(meta) """# now i have got all meta tags with their name 

# now i can find a particular meta tag using its name attribute

description_tag = soup.find('meta', attrs={"name":"keywords"})
keywords_content = description_tag['content'].strip()
# print(f'Keyword Content: {keywords_content}')


website_details = {
  "h2 heading": headings,
  "keyword_description": keywords_content,
  "title": title
}

# print(f"Website Details: {website_details}")