#To check weather the number is prime or not

num = int(raw_input("input a number "))
flag=0
for i in range(1,num+1):
    if num % i==0:
        flag=flag+1
print flag

if flag > 2:
    print "No is not prime"
else:
    print "No is prime"
