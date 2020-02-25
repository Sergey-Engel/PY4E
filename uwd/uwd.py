# uwd - URL Watch Dog
#
# To run this, install the BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter URL: ')
resource = ''
if len(resource) < 1 :
    resource = 'ai-news.ru'
url = 'https://'+resource+'/'
fname = resource+'.txt'
flog = resource+'.log'

try:
    html = urlopen(url, context=ctx).read()
except:
    print('ERROR -- URL \"'+url+'\" can not be open')
    quit()

urloldlist = list()
try:
    foh = open(fname,'r')
    for oldline in foh :
        urloldlist.append(oldline)
except:
    print('WARNING -- File \"'+fname+'\" can not be open')

try:
    flh = open(flog,'a')
except:
    print('ERROR -- File \"'+flog+'\" can not be open')
    quit()

soup = BeautifulSoup(html, "html.parser")
tags = soup('a')

urllist = list()
for tag in tags : urllist.append(tag.get('href', None))
urllist.sort()
urlnewlist = list()

prevline = ''
for line in urllist :
    if line == prevline : continue
    urlnewlist.append('https://ai-news.ru/'+line+'\n')
    prevline = line

lennew = len(urlnewlist)
lenold = len(urloldlist)
print('Total NEW links:',lennew)
print('Total OLD links:',lenold)

new = 0
old = 0

for i in range(0,max(lennew,lenold)) :
#for i in range(0,20) :
    if new > lennew-1 :
        print('--- ('+str(old)+'): '+urloldlist[old].rstrip())
        flh.write('--- ('+str(old)+'): '+urloldlist[old].rstrip()+'\n')
        old = old + 1
        continue
    if old > lenold-1 :
        print('+++ ('+str(new)+'): '+urlnewlist[new].rstrip())
        flh.write('+++ ('+str(new)+'): '+urlnewlist[new].rstrip()+'\n')
        new = new + 1
        continue
    if urlnewlist[new] > urloldlist[old] :
        print('--- ('+str(old)+'): '+urloldlist[old].rstrip())
        flh.write('--- ('+str(old)+'): '+urloldlist[old].rstrip()+'\n')
        old = old + 1
        continue
    if urlnewlist[new] < urloldlist[old] :
        print('+++ ('+str(new)+'): '+urlnewlist[new].rstrip())
        flh.write('+++ ('+str(new)+'): '+urlnewlist[new].rstrip()+'\n')
        new = new + 1
        continue
    if urlnewlist[new] == urloldlist[old] :
        new = new + 1
        old = old + 1
        continue

# Write new information into file
try:
    fnh = open(fname,'w')
except:
    print('ERROR -- File \"'+fname+'\" can not be open')
    quit()
for line in urlnewlist: fnh.write(line)
