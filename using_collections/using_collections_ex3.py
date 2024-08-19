# 3. Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2).

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)[::-1]
reversed_tuple = tuple(my_list[1:len(my_list) - 1])
print(reversed_tuple)

# ls solution
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
result = tuple(my_list[1:4])
print(result)   # (4, 3, 2)

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)   # (4, 3, 2)

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-3:-5:-1]
print(result)   # (4, 3, 2)

