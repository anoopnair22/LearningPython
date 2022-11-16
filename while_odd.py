## even number program (while)
x = int(input("Enter a number: "))
print("you entered <", x, ">")
y = int(input("How many odd numbers you wish to print? "))
print("Printing", y, "odd3 numbers after ", x)

if x % 2 == 0:
    z = x + 1
    i = 0
    while i < y:
        print(z)
        z = z + 2
        i=i+1
else:
    z = x + 2
    i = 0
    while i < y:
        print(z)
        z = z + 2
        i = i + 1
