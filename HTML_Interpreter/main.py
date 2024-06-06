with open("index.html") as f:
    html_doc = f.read()
from pythonmonkey import require as js_require

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')

print(soup.title.string)
print(soup.a)