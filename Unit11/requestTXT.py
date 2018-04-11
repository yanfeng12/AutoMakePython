import requests


res = requests.get('http://www.gutenberg.org/files/98/98-0.txt')
try:
    res.raise_for_status()
    with open('A Tale of Two Cities.txt','wb') as playFile:
        for chunk in res.iter_content(100000):
            playFile.write(chunk)
except Exception as exc:
    print('There was a problem: %s' %(exc))
