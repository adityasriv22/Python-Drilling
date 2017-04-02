"""
Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. O(n^2).The second function should be linear O(n).
"""

import time
from random import randrange
def findmin(l):
   overallmin=l[0]
   for i in l:
      issmallest=True
      for j in l:
         if i > j:
            issmallest=False
      if issmallest:
         overallmin=i
   return overallmin

print(findmin([5,4,2,1,0]))

