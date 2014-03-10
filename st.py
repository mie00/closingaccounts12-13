# coding=utf-8
import re
import sys
with open("st.txt") as f:
	r=f.read().split('\n')
def write(x):
	with open("op.txt",'w') as f:
		f.write(x)

write('\n'.join(filter(lambda x:re.findall(".+[\d+]$",x),r)))
print len(r)
#print unichr(1578)
