l=[2,3,4,1,9]
start=0
for i in range(start,len(l)):
	if l[i] < l[start]:
		l[start]=l[i]

print l
