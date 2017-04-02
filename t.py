"""
l=[1122,534,55,111]
s=min(l)
print s
"""

def checkAnagram(a,b):
	l=list(b) #for comparision
	p1=0 #starting point of string 
	stilOK=True #boolean condition
	while p1 < len(a) and stilOK:#traverse string 1

		p2=0
		found=False
		while p2 < len(l):#traverse string 2
			if a[p1]==l[p2]:
				found=True
			else:
				stilOK=False
		p1=p1+1#iterate over next alphabet
	return stilOK






print(checkAnagram("nitin","tinin"))