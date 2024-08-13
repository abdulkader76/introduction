# What are sets?

# sets type maintain an unordered collection of unique objects.

# unordered collection - no pre-determined order for sets

# unique objects (elements) - no duplicate values in sets

# 2 types of sets
# sets          - mutable
# frozen sets   - immutable

letters = {'a', 'b', 'c'}
letters.add('d')
print(letters)      # {'b', 'a', 'd', 'c'}

# frozen_letters = frozenset(letters)
# frozen_letters.add('e')
# AttributeError: 'frozenset' object has no attribute 'add'

# sets, frozensets - heterogenous
# contain multiple objects

# e.g.
my_set = {
    'May',
    2.99,
    (None, True, False),
    range(5),
}

# Python ignores any duplicate members in a set
letters = {'a', 'b', 'c', 'b', 'a'}
print(letters)      # {'a', 'b', 'c'}

letters.add('c')
print(letters)

# after 3.7, Python integers seem to be ordered
numbers = {1, 2, 3, 4, 5}
print(numbers)      # {1, 2, 3, 4, 5}

numbers = {5, 3, 1, 2, 4}
print(numbers)      # {1, 2, 3, 4, 5}

# The printing of both sets with the same ordered values is an illusion

numbers = {1, 2, 37, 4, 5}
print(numbers)


numbers = {1, 2, 3, 4, 5}
print(numbers)      # {1, 2, 3, 4, 5}

numbers = {5, 3, 1, 2, 4}
print(numbers)      # {1, 2, 3, 4, 5}

numbers_sets = {5, 2, 1, 37, 4}
print(numbers_sets)      # {1, 2, 4, 37, 5}