import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# Open and Close Connection
my_url = 'https://www.dailyfx.com/sentiment-report'
uClient = uReq(my_url) 
page_html = uClient.read()
uClient.close()

# HTML Parsing
page_soup = soup(page_html, "html.parser" )

# Finding the elements to scrape

containers = page_soup.findAll("span", {"class":"gsstx"})



# Useful bs4 Tools from docs
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
            
# us_oil = container.findAll("",{":"})

# print(page_soup.prettify())
# page_soup.get_text()

# for link in page_soup.find_all('a'):
# print(link.get('href'))

