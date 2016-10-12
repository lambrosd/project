
s = input("Enter binary number: ")
a = list(s)
a = [int(s) for s in a]

count = 0
for s in range(0,8):
    if a[s]==1:
        count=count + 1
if count%2==0:
    print("Parity check OK.")     
else:
    print("Parity check not OK.")


