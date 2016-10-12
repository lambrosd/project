
s = input("Enter Tax Identification Number: ")
a = list(s)
a = [int(s) for s in a]

sum =((a[7]*(2**1)) + (a[6]*(2**2)) + (a[5]*(2**3)) + (a[4]*(2**4)) + (a[3]*(2**5)) + (a[2]*(2**6)) + (a[1]*(2**7)) + (a[0]*(2**8)))
remainder = sum%11

if (remainder%10) == a[8]:
    print('Tax identification Number valid')
else:
    print('Tax identification Number not valid')

