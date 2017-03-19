#a=int(raw_input("Enter a number two check if its armstrong or not"))
for i in range(100,900):
	t1=i%10
	i=i/10
	t2=i%10
	t3=i/10
	sum=0
	sum=t1**3+t2**3+t3**3
	if i==sum:
			print "I is armstrong",i

