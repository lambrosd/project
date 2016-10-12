s = input("Enter 9 digit number: ")
a = list(s)
a = [int(s) for s in a]

for s in range(0,8,3):
        print(a[s],end='  ')
print(' ')
for s in range(1,9,3):
        print('',a[s],end=' ')
print(' ')
for s in range(2,10,3):
        print(' ',a[s],end='')
