# Comparing Collections

# python supports comparison for collections

# equality '==' straightforward comparison
# - same type (list, tuple, etc)
# - equal number of elements
# - sequences, each pair of corresponding elements are equal
# - sets - each sets has the same members (order not required)
# - maps, key/value pair must be present & identical in both maps (order not required)

# e.g
print([2, 3] == [2, 3]) # True
print([2, 3] == [3, 2]) # False
print([2, 3] == [2])    # False
print([2, 3] == (2, 3)) # False
print({2, 3} == {3, 2}) # True

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
dict3 = {'a': 1, 'b': 2, 'c': 3}

print(dict1 == dict2)   # True
print(dict1 == dict3)   # False

# != can also be used
# <, <=, >, >= can be used but rarely needed
