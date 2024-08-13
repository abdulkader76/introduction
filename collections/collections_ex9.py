my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

# 1. Are the lists assigned to my_list and another_list equal? 

# Yes, they have the same values, so when doing the '==' comparison, it will return True

# 2. Are the lists assigned to my_list and another_list the same object? 

# No, it can be determined when 'is' is used to compare the two objects. They may have the same values but are referencing different objects.

# 3. Are the nested lists at index 3 of my_list and another_list equal? 

# Yes, they have the same values and when using '==' operator, Python will return True

# 4. Are the nested lists at index 3 of my_list and another_list the same object? 

# Yes, when Python makes copies of the list, it will perform what is called a 'shallow copy', so when it compares the 2 objects, it will return True.

# launchschool solution:

# 1. The two lists are equal: they are both lists with the same elements.

# 2. The two lists are not the same object: The list constructor creates a new object.

# 3. The two nested lists are equal: they are both lists that have the same elements.

# 4. The two nested lists are the same object: the list constructor creates a shallow copy of the iterable passed as an argument. Shallow copies don't create new nested lists. Instead, only a reference to the nested list gets copied.
