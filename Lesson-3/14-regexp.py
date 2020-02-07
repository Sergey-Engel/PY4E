# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
import re

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
handle = open(name)

sum = 0
for line in handle :
    numlist = re.findall('[0-9]+',line)
    for number in numlist :
        sum = sum + int(number)
print(sum)
