# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mailCount = dict()
for line in handle :
    curWordSet = line.rstrip().split(' ')
    if len(curWordSet) < 1 or curWordSet[0] != 'From:' : continue
    mailCount[curWordSet[1]] = mailCount.get(curWordSet[1],0) + 1
bigcount = None
bigfrom = None
for address,count in mailCount.items() :
    if bigcount is None or count > bigcount :
        bigcount = count
        bigfrom = address
print(bigfrom,bigcount)
