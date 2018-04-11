import bs4


with open ('example.html') as exampleFile:
    exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
    elems = exampleSoup.select('#author')
    print(type(elems))
    print(len(elems))
    print(str(elems[0]))
    print(elems[0].attrs)

