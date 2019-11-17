from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the tr tags
tags = soup("tr")
total = 0
for tag in tags:
    # Look at the parts of a tag
    try:
        marks = int(tag.contents[1].contents[0].contents[0])
    except:
        continue
    total += marks

print(total)
