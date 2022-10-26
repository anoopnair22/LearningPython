def add(x,y):
    return int(x)+int(y)

def sub(x,y):
    return int(x)-int(y)

def mul(x,y):
    return int(x)*int(y)

def div(x,y):
    return int(x)/int(y)

def powr(x,y):
    return int(x)**int(y)

print("Confirm the operation required:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Power")

cmd = input("enter operator: ")
p = input("enter first input: ")
q = input("enter second input: ")

if int(cmd) == 1:
    print ("first input" + p, "second input" + q, "answer", add(p, q))
elif int(cmd) == 2:
    print("first input" + p, "second input" + q, "answer", sub(p, q))
elif int(cmd) == 3:
    print("first input" + p, "second input" + q, "answer", mul(p, q))
elif int(cmd) == 4:
    print("first input" + p, "second input" + q, "answer", div(p, q))
elif int(cmd) == 5:
    print("first input" + p, "second input" + q, "answer", powr(p, q))

else:
    print("wrong operator selected")
    exit()





