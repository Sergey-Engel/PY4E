# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mailByHours = dict()
for str in handle :
    curStr = str.split()
    if len(curStr) < 5 or curStr[0] != 'From' : continue
    curTime = curStr[5].split(':')
    curHour = curTime[0]
    mailByHours[curHour] = mailByHours.get(curHour,0) + 1

for k,v in sorted(mailByHours.items()) :
    print (k,v)
