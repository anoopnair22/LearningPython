## fibonacci series program (while)
start_num = int(input("Enter a number: "))
print("you entered <", start_num, ">")
pnum = int(input("How many fibonacci numbers you wish to print? "))
print("Printing", pnum, "fibonacci numbers after ", start_num)
count = 0
a = 0
b=1
if start_num ==1:
    print(b)
    pnum=pnum-1
if start_num<0:
    print(a)
while count <pnum:
    if b > start_num:
        print(a)
    else:

        pnum += 1
    if a >= -1:

        c = a + b
        a = b
        b = c
        # print(out)
    count += 1





