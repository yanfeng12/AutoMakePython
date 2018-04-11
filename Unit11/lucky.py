#! python3
# lucky.py - Opens several Baidu search results.


import requests, sys, webbrowser, bs4, pyperclip


print('Searching..........')
if len(sys.argv) >1:
    res = requests.get('https://cn.bing.com/search?q=' + ''.join(sys.argv[1:]))
    print('https://cn.bing.com/search?q=' + ''.join(sys.argv[1:]))
else:
    res = requests.get('https://cn.bing.com/search?q=' + pyperclip.paste())
    print('https://cn.bing.com/search?q=' + pyperclip.paste())
res.raise_for_status()
print(res.text)

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")



# Open a browser tab for each reesult.
linkElems = soup.select('a[href]')
print(linkElems)
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    print(linkElems[i].get('href'))
    webbrowser.open(linkElems[i].get('href'))
