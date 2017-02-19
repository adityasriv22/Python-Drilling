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
        p=l[i]
        t.append(p)
    else:
        print "There are no prime numbers in the list"
print t
"""
a = 0
temp = 0
b = 1
m = int(raw_input(";  "))
for i in range(0,m):
    a = temp
    temp = a + b
    b = a
    print a
