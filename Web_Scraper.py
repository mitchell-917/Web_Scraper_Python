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

us_oil = page_soup.findAll("a", {"class":"gsstx"})
us_30 = page_soup.findAll("a", {"class":"gsstx"})


