"""/*
#include<stdio.h>
#include<conio.h>
void main()
{
   int a[20], i, j, k, n;
   clrscr();
   
   printf("\nEnter array size : ");
   scanf("%d",&n);

   printf("\nEnter %d array element : ", n);
   for(i = 0; i < n; i++) 
   {
      scanf("%d",&a[i]);
   }
   
   printf("\nOriginal array is : ");
   for(i=0;i< n;i++)
   {
      printf(" %d",a[i]);
   }

   printf("\nNew array is  : ");
   for(i=0; i < n; i++) //1,2,3,2,5,6
   {
      for(j=i+1; j < n; )
      {
         if(a[j] == a[i])
         {
            for(k=j; k < n;k++) 
            {
               a[k] = a[k+1];
            }
            n--;
         }
         else {
            j++;
         }
      }
   }

   for(i=0; i < n; i++)
   {
      printf("%d ", a[i]);
   }
getch();
}
*/

l2=[]
l=[1,1,2,11,23,1,1,2]
count=0
for i in l:
   q = l.index(i)
   for j in l:
      r=l.index(j)
      if q == r:   
         print "Same Value Counter"
      else:
         if i == j:
            count+=1
            l2.append(i)
   if count > 1:
      print "Duplilcate elements: ",l2
      count =0
      del l2[:]
"""      
l2=[]
l=[1,1,2,11,23,1,1,2,23,45,78,87,65,45]
count=0
for i in l:
   for j in l:
      

      if i == j:
         count+=1
   if count > 1:
      l2.append(i)
   if i in l2:
      l2.pop(i)
   count=0
print l2

"""
   for j in l:
      if i == j:
         count+=1
   if count > 1:
      print i
      l2.append(i)
   count = 0
print l2
"""









