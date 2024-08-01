# print function

# works with most data types
# outputs something that makes it understandable to humans
print({'a': 1, "b": 42, 'c': "string", 'd': [5, 6], 'e': {8, 9, 10}})

import time
print(time.asctime())


# print multiple objects, by listing them one after the other
print(1, 2, 3, 'a', 'b')

print([1, 2, 3], 4, False, {5, 6, 7, 8})


# by default, objects are separated by white space, use sep keyword to change delimiter
print(1, 2, 3, 'a', 'b', sep=",")

# use empty string to join all the objects 
print('a', 'b', 'c', 'd', 'e', sep="")

# end keyword defines what print prints after printing output
print(1, 2, 'a', 'b', sep=',', end=' <= \n')


# use semi-colon to join multiple lines on a single line; mainly for REPL
print('a', 'b', end='', sep=','); print('c', 'd', sep=',')

# to start a new line without printing anything
print()
