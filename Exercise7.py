
a = int(input('Enter number of prionic numbers: '))
x = 0
for i in range(1,a):
    x = int(i*(i+1))
    i+=1
    print (int(x),end=' ')    
