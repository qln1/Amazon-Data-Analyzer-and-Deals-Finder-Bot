from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import xlwt
import xlrd
import os


set_discount = 60

# #### Alternate method to get html data from website
# # URl to web scrap from.
# # In this example we web scrap discounts Electronic from Amazon
# # Interchangeable if needed
# my_url = "https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb_40dff72b654a4d9e977a0d06d9b4038f&deals-widget=%257B%2522version%2522%253A1%252C%2522viewIndex%2522%253A0%252C%2522presetId%2522%253A%25226166F99AC29FCB0619968DE135E9B661%2522%252C%2522departments%2522%253A%255B%2522172282%2522%255D%252C%2522sorting%2522%253A%2522BY_CUSTOM_CRITERION%2522%257D"
# # this discount or higher
#
#
# uClient = uReq(my_url)
# page_html = uClient.read()
# uClient.close()
# page_soup = soup(page_html, "html.parser")
#
# # Finds all of the products on the web page
# containers = page_soup.findAll("div", {"class": "DealItem-module__dealItemContent_SGFPcLDYb5e-vSMK5SDH"})





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

    if discount >= set_discount:
        product_name_hold = single_cont.findAll("div", {"class": "DealCard-module__truncate_3E_98PYsAQzbYk0BLscdkC"})
        product_name = product_name_hold[0].text.strip()
        single_product_info.append(product_name)

        all_products.append(single_product_info)









# #### Tips
# # helpful if you know the path of the information you want
# # brand is a string saying the brand of the product
# brand = single_cont.div.div.a.img["title"]
#
# # if don't know the path directory, then use this find all method to find all instances where it's in a list "li"
# # And the class name is "price-ship"
# # The method will return an array of all instances that have been found
# # (usually if only one is found just use shipping_container[0])
# shipping_container = single_cont.findAll("li", {"class": "price-ship"})
# # text means the text part of this
# # strip() takes away all the html tags like </a>, leaving only the string text that we need
# shipping = shipping_container[0].text.strip()