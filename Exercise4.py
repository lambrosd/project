import math
x1 = float
x2 = float
x = float
a = int(input("Enter values for a: "))
b = int(input("Enter values for b: "))
c = int(input("Enter values for c: "))

d = int(b**2 - 4*a*c)

if d < 0:
    print('This equation has no real solutions.')
    
elif d == 0:
    x = float(-b / (2*a))
    print('This equation has sole solution which is ' ,x)
    
else: # if d > 0
    x1 = float((-b + math.sqrt(d))/(2*a))
    x2 = float((-b - math.sqrt(d))/(2*a))
    print('This equation has two solutions which are ' ,x1, x2)
