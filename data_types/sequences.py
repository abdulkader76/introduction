# Exampe of lists
# my_list = [1, 'xyz', True, [1, 2, 3]]

# Example of tuples
# tup = ('xyz', [2, 3, 4], 1, True)

# Example of list and tuple - multiline format
# [ # Begin multi-line list literal
    # "Monty Python's Flying Circus",
    # ( # Begin multi-line tuple literal
    #     'Eric Idle',
    #     'John Cleese',
    #     'Terry Gilliam',
    #     'Grahan Chapman',
    #     'Michael Palin',
    #     'Terry Jones',
    #    ) # End multi-line tuple literal
# ] # End multi-line list literal
    
# trailing commas on last items - optional
# but considered good practice

# my_list = [1, 'xyz', True, [2, 3, 4]
# my_list[0] --> 1
# my_list[1] --> 'xyz'
# my_list[2] --> True
# my_list[3] --> [2, 3, 4]
# my_list[4] --> IndexError: list index out
#                               of range

# Lists - mutable
# Tuples - immutable

# my_list[3] = 'New value'
# my_list
# [1, 'xyz', True, "New Value"]

# tup[3] = "New value"
# TypeError: 'tuple' object does not support
#               item assignment

# Ranges

# tuple(range(5))
# (0, 1, 2, 3, 4)

# tuple(range(5, 10))
# (5, 6, 7, 8, 9)

# list(range(1, 10, 2))
# [1, 3, 5, 7, 9]

# list(range(0, -5, -1))
# [0, -1, -2, -3, -4]

# my_range = range(5, 10)
# my_range[3] --> 8

# Maps

# my_dict = {
#     'dog': 'barks',
#     'cat': 'meows',
#     'pig': 'oinks',
#     'chicken': 'clucks',
#     'cow': 'moos',
#     'duck': 'quacks',
# }

# m

my_dict = {
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks',
}

# my_dict['dog']
# 'barks'

# my_dict['cat']
# 'barks'

# my_dict['pig']
# 'oinks'

# my_dict['bird']
# KeyError: 'bird'

# my_dict['cat'] = 'purrs'
# {
#     'dog': 'barks',
#     'cat': 'purrs',
#     'pig': 'oinks',
# }

# dic = {}
# dic['a'] = 1
# dic['b'] = 2
# print(dic)    # {'a': 1, 'b': 2}
# del dic['a']
# dic['a'] = 1
# print(dic)    # {'b': 2, 'a': 1}

# d1 = {}
# print(type(d1))
# <class dict>

# s1 = set()
# print(s1)
# set()

# Create a set from a literal
# s2 = {2, 3, 5, 7, 11, 13}
# print(s2)
# {2, 3, 5, 7, 11, 13}

# Create a set from a string
# s3 = set("hello there!")
# {'t', 'o', 'e', 'l', ' ', 'h', '!', 'r'}

# Example of a set in multi-line format
# monty_python_cast = {
#     'Eric Idle',
#     'John Cleese',
#     'Terry Gilliam',
#     'Graham Chapman',
#     'Michael Palin',
#     'Terry Jones',
# }

# s5 = frozenset([1, 2, 3])
# print(s5)
# frozenset({1, 2, 3})

# s6 = frozenset((1, 2, 3))
# print(s6)
# frozenset({1, 2, 3})

# s7 = frozenset({1, 2, 3})
# print(s7)
# frozenset({1, 2, 3})

# s8 = frozenset(range(1, 4))
# print(s8)
# frozenset({1, 2, 3})
