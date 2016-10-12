import math
area = float
d = int
input_a = int(input("Give me side a of the triangle: "))
a = input_a
input_b = int(input("Give me side b of the triangle: "))
b = input_b
input_c = int(input("Give me side c of the triangle: "))
c = input_c

d = (a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c)
area = float( math.sqrt(d)/4)

print('The area of the triangle is %0.2f' %area)
