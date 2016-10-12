
y = int(input("Enter year: "))

a = y%4
b = y%7
c = y%19
d = (19*c + 15)%30
e = (2*a + 4*b - d + 34)%7
month = (d + e + 114)//31
day = ((d + e + 114)%31) + 1
day = day + 13

for y in range(1900,2099,4):
    if (day>=30 and month==2):
        day = day-29
        month=month+1
        print("Day:",day, "Month:", month, end = ' ')
if (day>=29 and month==2):
    day = day-28
    month=month+1
    print("Day:",day, "Month:", month, end = ' ')
elif (day>=31 and (month == 4 or month == 6 or month == 9 or month == 11)):
    day = day-30
    month=month+1
    print("Day:",day, "Month:", month, end = ' ')
elif (day>=32 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12)):
    day = day-31
    month=month+1
    print("Day:",day, "Month:", month, end = ' ')
else:
    print("Day:",day, "Month:", month, end = ' ')
    

