## even number program
x = int(input("Enter a number: "))
print("you entered <", x, ">")
y = int(input("How many even numbers you wish to print? "))
print("Printing", y, "even numbers after ", x)

if x % 2 == 0:
    z = x + 2
    for i in range(y):
        print(z)
        z = z + 2
else:
    z = x + 1
    for i in range(y):
        print(z)
        z = z + 2
