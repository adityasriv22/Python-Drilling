def linearsearch(l,d):
	for i in l:
		if i == d:
			print "found"
			
	else:
		print "no found"


l1=[2,4,5,6,4,78]
a =int(raw_input("Enter a num to find "))
linearsearch(l1,a)