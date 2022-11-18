#string operations - indexing
my_list = ['Red', 'Green', 'Brown', 'yellow', 1, 2, 3, ['a','b','c']]

length = int(len(my_list))

print("The list is: ", my_list )
print("First character in list is: ", my_list[0])
print("Last character in list is: ", my_list[-1] )
print("Length of input is: " , length)

if length % 2 != 0:
    print("Middle value is: ", my_list[int(length/2)])
else:
    print("Middle value is: ", my_list[int(length/2 - 1)], my_list[int(length/2 + 1)])

