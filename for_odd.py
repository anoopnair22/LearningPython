## odd number program
x = int(input("Enter a number: "))
print("you entered <", x, ">")
y = int(input("How many odd numbers you wish to print? "))
print("Printing", y, "odd numbers after ", x)

if x % 2 == 0:
    z = x + 1
    for i in range(y):
        print(z)
        z = z + 2
else:
    z = x
    for i in range(y):
        z = z + 2
        print(z)
