
x = input("Enter numbers: ")
a = x.split()
for x in range(0,9,3):
        print(' ',a[x],end='|')
print('')
for x in range(1,9,3):
        print('',a[x],end='|')
print('')
for x in range(2,9,3):
        print(a[x],end='|')
