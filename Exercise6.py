
a = int(input('Enter number of triangle numbers: '))
n=1
x=0

for i in range(a):
   x = int((n*(n+1))/2)
   n = n+1
   print (int(x),end=' ')
