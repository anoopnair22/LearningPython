## fibonacci series program (while)
start_num = int(input("Enter a number: "))
print("you entered <", start_num, ">")
count = int(input("How many fibonacci numbers you wish to print? "))
print("Printing", count, "fibonacci numbers after ", start_num)
#i = 0
#b = x
#a = 0
#print (x)
#while i < y:
#    print(b)
#    c = a + b
#    a = b
#    b = c
#    i=i+1

a = 0
b = 1

if start_num < 0:
    if count == 1:
        print ('0')
    elif count == 2:
        print ("0", "1")
    elif count == 3:
        print ("0", "1", "1")
    elif count > 3:
        print("0", "1", "1")
        count = count - 3
        a = 1
        b = 1
elif start_num == 0:
    if count == 1:
        print('1')

    elif count == 2:
        print("1", "1")
    elif count > 2:
        print("1", "1")
        count = count - 2
        a = 1
        b = 1
elif start_num == 1:
    if count == 1:
        print('1')

    elif count > 1:
        print("1", "1")
        count = count - 1
        a = 1
        b = 1
elif start_num > 1:
    print("hi")
    print (count)
    if count > 0:
        c = a + b
        if c > start_num:
            print(c)
            count = count - 1
            a = b
            b = c

