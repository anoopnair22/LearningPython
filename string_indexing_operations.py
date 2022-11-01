##string operations - indexing
str = input("enter a string: ")
length = len(str)
mid = int(length/2)
value1 = str[:1]
value2 = str[-1]
value3 = int(length)

print("you entered: " + str)
print("First character in " + str, " is:" + value1)
print("Last character in " + str, " is:" + value2)
print("Length of string " + str, "is: " , length)

if length % 2 != 0:
    value4 = str[mid]
    print("Middle character in " + str, "is :" + value4)
else:
    value4= str[mid-1:mid+1]
    print("Middle characters in " + str, "is :" + value4)
