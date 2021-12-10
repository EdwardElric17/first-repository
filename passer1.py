import bs4, requests
def getpage(cssclass, adres):
    s = requests.get(adres).text
    parser = bs4.BeautifulSoup(s, "html.parser")
    massiv = parser.select(cssclass)
    for x in massiv:
        print(x.getText())
        print(x.attrs['href'])
getpage('.reference internal current', 'https://ipython.readthedocs.io/en/stable/')