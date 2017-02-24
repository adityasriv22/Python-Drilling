"""
logic behind the c language
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
"""

l=[]
k=int(raw_input("Enter the number of elements to add into the list: "))
for i in range(0,k):
    a=int(raw_input("+_+ : "))
    l.append(a)
print l
l2=[]
for i in range(len(l)):
   c=l.count(i)  
   if c > 1:
      l2.append(l[i])
print l2

            
