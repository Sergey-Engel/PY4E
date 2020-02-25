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

fname = 'ai_news.txt'
foldname = 'ai_news_old.txt'
try:
    fh = open(fname,'w')
except:
    print('ERROR -- File \"'+fname+'\" can not be open')
    quit()
try:
    foh = open(foldname,'r')
except:
    print('ERROR -- File \"'+foldname+'\" can not be open')
    quit()

#print('TAG',tag)
#print('URL-'+str(count), tag.get('href', None))
#print('CONTENT',tag.contents[0])
#print('ATTRs:', tag.attrs)

urllist = list()
for tag in tags : urllist.append(tag.get('href', None))
urllist.sort()
urlnewlist = list()

prevline = ''
for line in urllist :
    if line == prevline : continue
    urlnewlist.append('https://ai-news.ru/'+line+'\n')
    prevline = line

for line in urlnewlist: fh.write(line)

urloldlist = list()
for oldline in foh :
#    oldline.rstrip()
    urloldlist.append(oldline)

print('Total NEW links:',len(urlnewlist))
print('Total OLD links:',len(urloldlist))

new = 0
old = 0
for i in range(0,max(len(urlnewlist),len(urloldlist))) :
#for i in range(0,20) :
    if urlnewlist[new] == urloldlist[old] :
        new = new + 1
        old = old + 1
        continue
    if urlnewlist[new] > urloldlist[old] :
        print('--- ('+str(old)+'):',urloldlist[old].rstrip())
        old = old + 1
        continue
    if urlnewlist[new] < urloldlist[old] :
        print('+++ ('+str(new)+'):',urlnewlist[new].rstrip())
        new = new + 1
        continue
