#Take 5 inputs in an array find the max sum and min sum

l=[]
k=int(raw_input("Enter the number of elements to add into the list: "))
for i in range(0,k):
    a=int(raw_input("+_+ : "))
    l.append(a)
msum=0
l.sort(reverse=True) #Sorting the array in Descending order
for i in range(len(l)-1):
    msum=msum+l[i]

l.sort(reverse=False)# to bring back the normal list
print ("The maximmum sum of an array is: "),msum
#min sum
l1=l[:]
l1.sort()
minsum=0
for i in range(len(l)-1):
    minsum=minsum+l[i]
print ("The minimum sum of an array is: "),minsum