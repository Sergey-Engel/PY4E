# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_366163.json (Sum ends with 10)
# Data format:
#   <comment>
#       <name>Matthias</name>
#       <count>97</count>
#   </comment>

import urllib.request, urllib.parse, urllib.error
import json
import ssl

#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_366163.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

json_tree = json.loads(data.decode())
#print(json_tree)
allcomments = json_tree['comments']
#print(allcomments)

count = 0
sum = 0
for cc in allcomments :
#    print('Name:', cc['name'], 'Count:',cc['count'])
    count = count + 1
    sum = sum + int(cc['count'])
print('Count:',count)
print('Sum:',sum)
