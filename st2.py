# coding=utf-8
import re
import sys
with open("op.txt") as f:
	r=f.read().split('\n')
def write(x):
	with open("op3.txt",'w') as f:
		f.write(x)
def aa(c):
	print c
	return c
def find(fn,arr):
	a=reduce(lambda x,y:x or filter(fn,[y]),arr,[])
	if a:return a[0]
	return None
#write('\n'.join(filter(lambda x:len(re.findall("\t+",x))!=5,r)))
group={'00000000':None}
def maphelp((a,b)):
	group[a]=Thing(a,b)
class Thing:
	def __init__(self,number,cont):
		self.number=number
		self.cont=cont
		self.parent=parent(number)
		if self.parent:self.parent.addchild(self)
		self.children=[]
	def addchild(self,child):
		self.children.append(child)
def parent(number):
	z=[8,7,6,5,3,2,0]
	for i,j in enumerate(z):
		if j==8:continue
		if number[-j:]=='0'*j:
			try:
				return group[number[:-z[i-1]]+'0'*z[i-1]]
			except:
				print number
write('\n'.join(filter(lambda x:len(re.findall('\t+',x))==5,r)))
a=zip(map(lambda x:(re.search('\d+$',x).group(0)),r),r)
map(maphelp,a)
print group['20000000']
print find(lambda x:aa(x)>1,[-1,0,2])
print a[:10]
print len(r)
#print unichr(1578)
