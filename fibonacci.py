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

l = [12,34,44]
l1=l[:]
print l1