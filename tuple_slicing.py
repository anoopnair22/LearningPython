#tuple slicing

my_tuple = ("Red", "Green", "Blue", "Yellow", 1, 2, 3)
print (my_tuple)
print(type(my_tuple))
print("you entered: ", my_tuple)
print("Slice of value after removing first and last values:", my_tuple[1:-1])
print("Slice of value after removing first 2 values: ",  my_tuple[2:])
print("Slice of value after removing last 2 values: ", my_tuple[:-2])
print("mid value is",my_tuple[3])
print("First half slice is: ",my_tuple[0:3])
print("Last half slice is: ", my_tuple[4:])