
#tuple operations - indexing
my_tuple = ("Red", "Green", "Blue", "Yellow", 1, 2, 3)
print(my_tuple)
print(type(my_tuple))

length = int(len(my_tuple))

print("The tuple is: ", my_tuple )
print("First value in list is: ", my_tuple[0])
print("Last value in list is: ", my_tuple[-1] )
print("Length of input is: " , length)

if length % 2 != 0:
    print("Middle value is: ", my_tuple[int(length/2)])
else:
    print("Middle value is: ", my_tuple[int(length/2 - 1)], my_tuple[int(length/2)])
