from collections import Counter

import requests
from bs4 import BeautifulSoup, Comment

# get the comment from html page in order to look for rare chars in it.
URL = "http://www.pythonchallenge.com/pc/def/ocr.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
comment = soup.find_all(string=lambda text: isinstance(text, Comment))[1]

rarest_chars = Counter(comment).most_common()[-8:]
print(rarest_chars)  # equality
