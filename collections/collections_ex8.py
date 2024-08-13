# 8. How would you print all the numbers in the following range?

# range(3, 17, 4)
my_list = list(range(3, 17, 4))
print(my_list)          # [3, 7, 11, 15]

# launchschool solution
# solution 1
# print(list(range(3, 17, 4)))

# solution 2
# print(tuple(range(3, 17, 4)))

# Since ranges are lazy sequences, you must either iterate over the range or convert the range to a non-lazy sequence: a list or tuple. Here, we transform the range into a list and a tuple.

