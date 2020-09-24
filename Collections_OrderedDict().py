# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
import re

ord_dict= OrderedDict()
r = re.compile("([a-zA-Z]+)([0-9]+)")
t = int(input())
for i in range (t):
    entry = input()
    m = re.split(r'(\d+)',entry)
    item=m[0].rstrip()
    price=int(m[1])
    if item in ord_dict:
        ord_dict[item] = ord_dict[item]+price
    else:
        ord_dict[item] = price
for key, value in ord_dict.items():
    print('{} {}'.format(key, value))



