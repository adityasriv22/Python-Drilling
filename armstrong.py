
l=[2,3,5,55,5,1,11]
key = len(l) // 2
find = int(raw_input("Enter a number to find from the list"))
if key == find:
	print"Found the element"
elif key > find:
	for i in range(0,key):
		if i == find:
			print "Found by left"
else key < find:
	for i in range(key,len(l)):
		if i == find:
			print "Found by right"






