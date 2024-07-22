#Web scraping is the process of extracting data from websites. It involves retrieving and parsing the HTML of web pages to collect specific information. This data can then be used for various purposes such as analysis, aggregation, and integration into other systems.


#Key Concepts in Web Scraping
# Key Concepts in Web Scraping
# HTML Parsing: Analyzing the structure of the HTML code of a web page to locate and extract the desired data.
# HTTP Requests: Sending requests to web servers to retrieve the HTML content of web pages. Common methods include GET and POST requests.
# Web Crawling: Automated browsing of the web, where a bot navigates through links on web pages to collect data from multiple pages.
# Data Extraction: Identifying and extracting specific pieces of information from the HTML content, such as text, images, or links.
# Data Storage: Saving the extracted data in a structured format such as CSV, JSON, or directly into a database for further use.


# Tools and Libraries for Web Scraping
# BeautifulSoup: A Python library used for parsing HTML and XML documents. It provides methods to navigate and search the parse tree.
# Scrapy: An open-source web crawling framework for Python that provides a powerful and flexible way to extract data from websites.
# Selenium: A web testing library that can be used for web scraping, especially for dynamic content rendered by JavaScript.
# Puppeteer: A Node.js library that provides a high-level API to control Chrome or Chromium over the DevTools Protocol. Useful for scraping JavaScript-heavy websites.
# Requests: A simple and elegant HTTP library for Python to handle HTTP requests.
# Legal and Ethical Considerations
# Respect Robots.txt: Many websites include a robots.txt file that specifies which parts of the site can be accessed by bots. Respecting these guidelines is crucial.
# Terms of Service: Check the website’s terms of service to ensure that web scraping is allowed.
# Rate Limiting: Implement rate limiting to avoid overloading the website’s server with too many requests in a short period.
# Personal Data: Be mindful of scraping personal data, which may be subject to data protection laws like GDPR or CCPA.




# To find out if a website allows you to scrap or not.
#add the extension robots.txt

#Basic Example of Web Scraping with BeautifulSoup
# Here's a simple example of web scraping using Python's BeautifulSoup and Requests libraries to extract data from a web page:


import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the desired data
titles = soup.find_all('h2')  # For example, extracting all h2 elements

# Extract and print the text from the elements
for title in titles:
    print(title.get_text())




#another one


import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titleline > a') #heads up! .storylink changed to .titleline
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a') #heads up! .storylink changed to .titleline
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
