import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.macys.com/shop/product/polo-ralph-lauren-mens-classic-fit-linen-shirt?ID=9524093&CategoryID=20626&swatchColor=Summer%20Royal").content
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("h1", {"class":"page-header simple product-title large"})
title = span.text
span = soup.find("span", {"class":"money"})
price = span.text
span2 = soup.find("div", {"class":"form-field form-field-swatch swatch-other"})
colors = span2.text
print("Item %s has the price %s" % (title, price))
