# coding=utf-8
import re
import sys
with open("op3.txt") as f:
	r=f.read().split('\n')
def write(x):
	with open("op4.txt",'w') as f:
		f.write(x)
#write('\n'.join(filter(lambda x:len(re.findall("\t+",x))!=5,r)))

def maphelp((a,b)):
	group[a]=Thing(a,b)
group={'00000000':None}
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
	z=[8,7,6,5,4,2,0]
	for i,j in enumerate(z):
		if j==8:continue
		if number[8-j:]=='0'*j:
			try:
				#return number[:-z[i-1]]+'0'*z[i-1]
				return group[number[:-z[i-1]]+'0'*z[i-1]]
			except:
				print 'Error:',number
a=zip(map(lambda x:(re.search('\d+$',x).group(0)),r),map(lambda x:x.split('\t'),r))
map(maphelp,a)
