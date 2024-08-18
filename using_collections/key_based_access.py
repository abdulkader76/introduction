# Key-Based Access

# unlike indexing - key-based access in dicts(maps) uses the keys to access data
# usually are strings but not always
# integers also can be keys - which can lead to complexity as they can be mistaken for indexes 
# any hashable object can be keys (including built-in immutable types)

# e.g.
my_dict = {
    'a': 'abc',
     37: 'def',
     (5, 6, 7): 'ghi',
     frozenset([1, 2]): 'jkl',
}

print(my_dict['a'])             # 'abc'
print(my_dict[37])              # 'def'
print(my_dict[(5, 6, 7)])       # 'ghi'
print(my_dict[frozenset([1, 2])])   # 'jkl'
#print(my_dict['nothing'])       
# KeyError: 'nothing'

# in above example, string, integer, tuple, frozenset are used to access values
# if in case the value doesn't exist, Python will return a KeyError 
# to avoid KeyError, use my_dict.get() method - if keys exist, it will return the values and when keys are not found, it will return None by default

# e.g
my_dict = {
    'a': 'abc',
     37: 'def',
     (5, 6, 7): 'ghi',
     frozenset([1, 2]): 'jkl',
}

print(my_dict.get('a'))              # 'abc'
print(my_dict.get('nothing'))        # None
print(my_dict.get('nothing', 'N/A')) # N/A
print(my_dict.get('nothing', 100))  # 100

# assign new values with key-based access to the left '=' operator

my_dict = {
    'a': 'abc',
     37: 'def',
    (5, 6, 7): 'ghi',
    frozenset([1, 2]): 'jkl',
}

my_dict['a'] = 'ABC'
my_dict[37]  = 'DEF'
my_dict[(5, 6, 7)] = 'GHI'
my_dict[frozenset([1, 2])] = 'JKL'

print(my_dict)

# assign new keys to a dict
# e.g
my_dict['xyz'] = 'Hey There!'
print(my_dict)
print(my_dict['xyz'])       # 'Hey There!'

# mutable keys are not allowed in dicts
# e.g
# my_dict[[1, 2, 3]] = 'Hey There!'
# TypeError: unhashable type: 'list'
# 3 mutable collections:
# lists, dictionaries, sets

# e.g using a float for key
my_dict[3.141592] = 'Pi'
print(my_dict[3.141592])
print(my_dict)

# e.g using a range for key
my_dict[range(0, 5)] = 'Range for 5'
print(my_dict)
print(my_dict[range(0, 5)])