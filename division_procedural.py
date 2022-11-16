# modified procedural
x = input("enter first input")
print("first values is " + x)
y = input("enter second input")
print("second values is " + y)


if (int(x) <= 0 or int(y) <= 0):
    print("please enter positive/non zero values")
    exit()
else:
    print('result')
    z = int(x) / int(y)
    print(z)
