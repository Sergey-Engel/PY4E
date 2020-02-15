# To run this, install the BeautifulSoup


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1 :
    url = 'https://ai-news.ru/'
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")
tags = soup('a')

count = 0
for tag in tags :
    count = count + 1
    #print('TAG',tag)
    print('URL-'+str(count), tag.get('href', None))
    #print('CONTENT',tag.contents[0])
    #print('ATTRs:', tag.attrs)
