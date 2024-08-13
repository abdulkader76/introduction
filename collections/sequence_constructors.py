# Set constructors

# literals review
# 'Hello world!'        # str literal
# 3.141592              # float literal
# True                  # bool literal
# {'a': 1, 'b': 2}      # dict literal
# [1, 2, 3]             # list literal
# (4, 5, 6)             # tuple literal
# {7, 8, 9}             # set literal
# 12334                 # int literal
# frozenset({1, 2, 3})  # frozenset literal

# in python objects can be created using literals but in some cases, objects have to be created using constructors

# objects that can only be created using constructors include ranges, frozensets, empty sets

# String Constructor
# returns a string
# use str() or str(something) - can be any Python object

# str()             # returns empty string ''
# str('abc')        # returns 'abc'
# str(42)           # returns '42'
# str(3.141592)     # returns '3.141592'
# str(False)        # returns 'False'
# str(None)         # returns 'None'
# str(range(3, 7))  # returns 'range(3, 7)'
# str([1, 2, 3])    # returns '[1, 2, 3]'
# str(int)          # returns '<class int>'
# str(list)         # returns '<class list>'

# class Person: pass
# str(Person())
# returns '<__main__.Person object at 0x10da6fb30>'


# Range Constructor
# ranges - 3 forms of constructors
# range(start, stop, step)
# r = range(5, 12, 2)
# print(list(r))    #   [5, 7, 9, 11]

# r = range(12, 8, -1)
# print(list(r))    #   [12, 11, 10, 9]

# r = range(12, 5, 2)
# print(list(r))    #   [12, 10, 8, 6]

# create empty ranges
# where start >= stop and step is positive
# r = range(5, 5, 1)
# print(list(r))    # []

# where start <= stop and step is negative
# r = range(5, 7, -1)
# print(list(r))    # []

# 2.
# range(start, stop)
# if the step is omitted, the default value is 1.
# range(star, stop) is same as range(start, stop, 1)

# 3.
# is there is only 1 arg in range, e.g range(5), then the start is taken as default value 0. range(stop)
# range(stop) is same as range(0, stop, 1)

# ranges considered "lazy sequences". they don't show elemental values until program needs them. 

# to show elemental values, you can lists and tuples. Sets and frozensets can be used but they may not be in order.

# List, Tuple, Set and Frozenset Constructors

# above mentioned share similar constructor forms

# list() or list(iterable)
# tuple() or tuple(iterable)
# set() or set(iterable)
# frozenset() or frozenset(iterable)

# my_str = 'Python'
# my_list = list(my_str)
# print(my_list)
# ['P', 'y', 't', 'h', 'o', 'n']
# my_tuple = tuple(my_str)
# print(my_tuple)
# ('P', 'y', 't', 'h', 'o', 'n')
# my_set = set(my_str)
# print(my_set)
# {'y', 'h', 'n', 'o', 'P', 't'}

# use these constructors to duplicate another collection

# my_list = [5, 12, 2]
# another_list = list(my_list)
# id(my_list)
# 4525181568
# id(another_list)
# 4525182144
# print(my_list)
# [5, 12, 2]
# print(another_list)
# [5, 12, 2]
# my_list == another_list
# True
# print(my_list is another_list)
# False

# when doing '==' comparison, the value is True
# when doing 'is' comparison, the value is False

# both list objects may have the same values but are referenceing different objects


# my_list = [[1, 2, 3], [4, 5, 6]]
# another_list = list(my_list)

# print(my_list) # [[1, 2, 3], [4, 5, 6]]
# print(another_list) # [[1, 2, 3], [4, 5, 6]]

# print(my_list == another_list) # True
# print(my_list is another_list) # False

# print(my_list[0] is another_list[0]) # True
# print(my_list[1] is another_list[1]) # True

# my_list & another_list share the same values
# when doing '==' comparison, it returns True
# when doing 'is' comparison, it returns False

# when doing 'is' comparison for its nested lists, it returns True - in this case, list constructor makes a 'shallow' copy - tbc

# note - nested collections - subject to shallow copies

# when a string is passed into these constructors, it is iterated over and the characters are separated into a single element

# print(tuple("Python"))
# ('P', 'y', 't', 'h', 'o', 'n')


