##def leap(y):
##    return int(y) % 4


print("Leap year check")
x = input("enter the year: ")

if int(x) % 400 == 0:
    print("This is a leap year")
    exit()
##elif int(x) % 400 != 0 and int(x) % 100 == 0:
elif int(x) % 100 == 0:
    print("THis is a not leap year")
    exit()
elif int(x) % 4 == 0:
    print("This is a leap year")
    exit()
else:
    print("This is not a leap year")
    exit
