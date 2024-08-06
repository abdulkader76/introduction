# Mutating the caller

# when an method changes an object, it is known as mutating the caller

# e.g
# odd_numbers = [1, 3, 5, 7, 9]
# odd_numbers.pop()   # last element is removed from object
# print(odd_numbers)  # [1, 3, 5, 7]

# example of functions mutating their arguments

def add_new_number(my_list):
    my_list.append(9)

numbers = [1, 2, 3, 4, 5]
add_new_number(numbers)
print(numbers)  # [1, 2, 3, 4, 5, 9]

# list.append used to add new number to caller
# no caller; argument is mutated

# Poor practice: mutating the argument
# can be difficult to debug functions

# mutating caller is acceptable - built-in functions and methods are designed for that

# almost no built-in functions mutate their arguments

# example of returning a new object

def add_new_number(my_list):
    return my_list + [9]

numbers = [1, 2, 3, 4, 5]
new_numbers = add_new_number(numbers)
print(new_numbers)
print(numbers)

# How to know which methods mutate the caller and which don't?

# if the object is immutable, it's easy

# if the object is mutable (changeable), then the only way to know is to read doc or look at the source code
