#!/usr/bin/python

"""
l = []
n = int(raw_input("Enter the no of elements to enter    "))
for i in range(0,n):
    x=int(raw_input(">< "))
    l.append(x)
print (l)
for i in range(0, len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            print l[i]
"""

#To check weather the number is prime or not

"""
num = int(raw_input("?? "))
flag=0
for i in range(1,num+1):
    if num % i==0:
        flag=flag+1
print flag

if flag > 2:
    print "No is not prime"
else:
    print "No is prime"
"""
################################################
"""
#To check weather the number is prime or not from a user entered list
l=[]
k=int(raw_input("Enter the number of elements to add into the list: "))
for i in range(0,k):
    a=int(raw_input("+_+ : "))
    l.append(a)

count=0
t=[]
for j in range(1,len(l)):
    if l[j] % j==0:
        count=count+1

    if count < 2:
        p=l[j]
        t.append(p)
    else:
        break
print t
"""
"""
#To print the fibonacci series
a = 0
temp = 0
b = 1
m = int(raw_input(";  "))
for i in range(0,m):
    a = temp #0,1,2,3,5
    temp = a + b # 1,2,3,5,8
    b = a #0,1,2,3
    print a
"""
#Take 5 inputs in an array find the max sum and min sum
"""
l=[]
k=int(raw_input("Enter the number of elements to add into the list: "))
for i in range(0,k):
    a=int(raw_input("+_+ : "))
    l.append(a)
#Total  sum
"""
l=[12,345,678,23,12,68]
msum=0
for i in range(len(l)):
    #for j in range(len(l) - 1):
    if l[i]<l[i+1]:
        temp=l[i]
        l[i]=l[i+1]
        l[i+1]=temp #[12,45,53]

"""


print (l)
#min sum
