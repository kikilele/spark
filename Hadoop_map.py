#!/usr/bin/python
import sys
list1=[]
for line in sys.stdin:
    line=line.strip()
    words=line.split('\n')
    list1.append(words[0])
for x in range(len(list1)):
    print list1[x]
