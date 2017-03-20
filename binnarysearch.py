
l=[2,3,5,55,6,1,11]
l.sort()
print l
key = l[len(l) // 2]
print key
find = int(raw_input("Enter a number to find from the list"))
if key == find:
	print"Found the element"
elif find < key:
	for i in range(0,key):
		if i == find:
			print "Found by left"
elif find > key:
	for i in range(key,len(l)+1):
		if i == find:
			print "Found by right"






