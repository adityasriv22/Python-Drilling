"""
Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. O(n^2).The second function should be linear O(n).
"""
def minlistOnsquare():
   l=[]
   k=int(raw_input("Enter the number of elements to add into the list: "))
   for i in range(0,k):
      a=int(raw_input("+_+ : "))
      l.append(a)
      for j in l:
         temp=0
         if j > j+1:
            temp=j
            j=j+1
            j+1=temp
   print l

minlistOnsquare()


