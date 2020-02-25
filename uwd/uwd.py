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

#resource = input('Enter URL: ')
resource = ''
if len(resource) < 1 :
    resource = 'ai-news.ru'
url = 'https://'+resource+'/'
ftxt = resource+'.txt'
flog = resource+'.log'

try: flh = open(flog,'a')
except:
    print('ERROR -- File \"'+flog+'\" can not be open')
    quit()

try: html = urlopen(url, context=ctx).read()
except:
    print('ERROR -- URL \"'+url+'\" can not be open')
    quit()

urloldlist = list()
try:
    foh = open(ftxt,'r')
    for oldline in foh :
        urloldlist.append(oldline)
    foh.close()
except:
    print('WARNING -- File \"'+ftxt+'\" can not be open')
urloldlist.sort()


soup = BeautifulSoup(html, "html.parser")
tags = soup('a')

urltmplist = list()
for tag in tags : urltmplist.append(tag.get('href', None))
urltmplist.sort()

# Deleting duplicate HREFs
urlnewlist = list()
prevline = ''
for line in urltmplist :
    if line == prevline : continue
    urlnewlist.append('https://ai-news.ru/'+line+'\n')
    prevline = line

lennew = len(urlnewlist)
lenold = len(urloldlist)
print('Total NEW links:',lennew)
print('Total OLD links:',lenold)

# Setup the barrier to the end of lists
urlnewlist.append('zzzzzz\n')
urloldlist.append('zzzzzz\n')
new = 0
old = 0

#for i in range(0,max(lennew,lenold)) :
while old <= lenold and new <= lennew :
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
    fnh = open(ftxt,'w')
except:
    print('ERROR -- File \"'+ftxt+'\" can not be open')
    quit()

# Deleting last 'zzzzzz' list's element before writing
urlnewlist.pop()
for line in urlnewlist: fnh.write(line)
