l=[1,2,2,3,1]
a=l.count(2)




"""
k=int(raw_input("Enter the number of elements to add into the list: "))
for i in range(0,k):
    a=int(raw_input("+_+ : "))
    l.append(a)
"""
count = 0
l1=[]
for i in range(len(l)):
	for j in range(len(l)-1):
		count = l.count(l[j])
	print count
		              #[1,2,2,3,1]
	if count > 1:
		append=l[j]
		l1.append(a)

print l1	



