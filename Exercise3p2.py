s = input("Enter 10 digit number: ")
a = list(s)
a = [int(s) for s in a]

for s in range(0,10):
    if s%2==0:
        print(a[s],end=' ')
print(' ')
for s in range(0,10):
    if s%2!=0:
        print('',a[s],end='')

