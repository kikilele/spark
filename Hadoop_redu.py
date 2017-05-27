#!/usr/bin/python
from operator import itemgetter
import sys

value={}
for line in sys.stdin:
    words=line.split('\n')
    if words[0][0]=='\t':
       continue
    else:
       word=words[0].split()
       #print words[0]
       #print word[0]
       #print '%s\t%s' % (word[0],word[1])
       if str(word[0]) in value:
          value[word[0]].append(int((word[1].split('\t'[0]))[0]))
       else:
          value[word[0]]=[int((word[1].split('\t'[0]))[0])]
       #print value[word[0]]

for one in value:
    value[one].sort()
print value

key=sorted(value.items(),key=lambda d:d[0])
print key
