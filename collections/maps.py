# What are Maps?

# maps - unordered collections of key/value pairs of objects
# many types of maps - main focus will dicts (dictionary)

# mutable
# keys in dicts - unique; if you ad any similar key, only the value will change
# Keys are hashable values - hashable values are not always immutable - built-in immutable types are always hashable (strings, numbers, tuples, frozensets, None) - hashable and dict keys
# values in each key/value pair - object

# example of maps
d = {'a': 1, (1, 3): 3, 1: 'x'}
print(d)    # {'a': 1, (1, 3): 3, 1: 'x'}
print(d['a'])       # 1
print(d[(1, 3)])    # 3
print(d[1])         # 'x'

d['a'] = 'A'
print(d)