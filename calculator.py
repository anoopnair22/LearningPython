# calculator program

print("Confirm the operation required:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
cmd = input("enter operator: ")
x = input("enter first input: ")
y = input("enter second input: ")
if int(cmd) == 1:
    z = (int(x) + int(y))
    print(z)
elif int(cmd) == 2:
    z = (int(x) - int(y))
    print(z)
elif int(cmd) == 3:
    z = (int(x) * int(y))
    print(z)
elif int(cmd) == 4:
    z = (int(x) / int(y))
    print(z)
else:
    print("Sorry, cant continue")



