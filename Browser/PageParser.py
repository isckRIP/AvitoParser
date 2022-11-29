from bs4 import BeautifulSoup

class PageParser:
    def __init__(self):
        "..."

    def BS(self, source):
        root = BeautifulSoup(source, 'html.parser')
        el = root.find_all("a", {"class": 'contacts-info__value link'})
        print(el[0].text)
