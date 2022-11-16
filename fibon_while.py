## fibonacci series program (while)
x = int(input("Enter a number: "))
print("you entered <", x, ">")
y = int(input("How many fibonacci numbers you wish to print? "))
print("Printing", y, "fibonacci numbers after ", x)
i = 0
b = x
a = 0
print (x)
while i < y:
    print(b)
    c = a + b
    a = b
    b = c
    i=i+1
