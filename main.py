from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import xlwt
import xlrd
import os


set_discount = 60



import requests
# URl to web scrap from.
# In this example we web scrap discounts Electronic from Amazon
# Interchangeable if needed
page = requests.get("https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb_40dff72b654a4d9e977a0d06d9b4038f&deals-widget=%257B%2522version%2522%253A1%252C%2522viewIndex%2522%253A0%252C%2522presetId%2522%253A%25226166F99AC29FCB0619968DE135E9B661%2522%252C%2522departments%2522%253A%255B%2522172282%2522%255D%252C%2522sorting%2522%253A%2522BY_CUSTOM_CRITERION%2522%257D")

html_contents = page.text
page_soup = soup(html_contents, "html.parser")

# Finds all of the products on the web page
containers = page_soup.findAll("div", {"class": "all-slots"})





all_products = []


for single_cont in containers:
    single_product_info = []

    discount_hold = single_cont.findAll("span", {"class": "a-row a-spacing-micro"})
    discount = discount_hold[0].text.strip()