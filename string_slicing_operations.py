##string operations
str = input("enter a string: ")
length = len(str)
mid = int(length/2)
value1 = str[1:length-1]
value2 = str[2:]
value3 = str[ :-2]
value4 = str[0:int(mid)]
print("you entered: " + str)
print("Slice of " + str, "after removing first and last character is:" + value1)
print("Slice of " + str, "after removing first 2 characters is:" + value2)
print("Slice of " + str, "after removing last 2 characters is:" + value3)
print("mid index is", + mid)
if length // 2 == 0:
    value4 = str[:mid]
    value5 = str[mid:]
else:
    value4= str[:mid]
    value5= str[mid:]
print("First half slice of"  + str, "is :" + value4)
print("First half slice of"  + str, "is :" + value5)