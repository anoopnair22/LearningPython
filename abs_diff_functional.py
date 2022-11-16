
def abst (x,y):
    z= (int(x) - int(y))
    if z<0:
        print(abs(z))
    else:
        print(z)

p = input("enter first value ")
q = input("enter second value ")
abst(p,q)