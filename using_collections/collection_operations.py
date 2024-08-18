# Common Collection Operations

# Non-Mutating Operations for Collections
# all the operations mentioned work for mutable and immutable objects - they don't change the object - they return a NEW object

# Collection Membership

# 'in' & 'not in' operators 
# 'in' - returns True if item IN collection
# 'no in' - returns False if item NOT IN collection

seq = [4, 'abcdef', (True, False, None)]
print(4 in seq)                     # True
print(4 not in seq)                 # False
print('abcdef' in seq)              # True
print('abcdef' not in seq)          # False
print('cde' in seq[1])              # True
print('cde' not in seq[1])          # False
print('acde' in seq[1])             # False
print('acde' not in seq[1])         # True
print((True, False, None) in seq)   # True
print((True, False, None) not in seq) # False
print(3.14 in seq)                  # False
print(3.15 not in seq)              # True

my_dict = {
    'a': '123',
    'b': '456',
    'c': '789',
}

print('a' in my_dict)               # True
print('b' not in my_dict)           # False

# for maps, in (not in) checks the keys
# for strings, it checks the right string contains the left string


# Minimum and Maximum Members
# min and max - return min and max values in a collection
# values have to compatible with < & > ops

my_set1 = {1, 4, -9, 16, 25, -36, -63, -1}
my_set2 = {'1', '4', '-9', '16', '25', '-36', '-1'}

print(min(my_set1), max(my_set1))  # -63, 25 
print(min(my_set2), max(my_set2))  # -1, 4 

# min & max - can't be used in heterogenous collections

my_set = {1, 4, '-9', 16, '25', -36, -63, -1}
# min(my_set)
# TypeError: '<' not supported between instances of 'str' and 'int'

# max(my_set)
# TypeError: '>' not supported between instances of 'str' and 'int'

my_set = {1, 3.14, -2.71}
print(min(my_set))      # -2.71
print(max(my_set))      # 3.14

# use min & max with mulitple arguments instead of an iterable
print(min(3, 5, -1), max(3, 5, -1)) # -1, 5


# Summation
# 'sum' used with iterable collections that are made up entirely of numeric values (integers, floats) - returns sum of all values

numbers = (1, 1, 2, 3, 5, 8, 13, 21, 34)
print(sum(numbers))             # 88

# for strings, use string.join() for string concatenation


# Locating Indices and Counting
# index & count
# index method returns the first element in the sequence that matches the given object
# count method returns the number of times a given object occurs in the sequence

# e.g index method
names = ['Karl', 'Grace', 'Clare', 'Victor', 'Antonina', 'Allison', 'Trevor']
print(names.index('Clare'))     # 2
print(names.index('Trevor'))    # 6
# print(names.index('Chris'))     
# ValueError: 'Chris' is not in list

numbers = [1, 3, 6, 5, 4, 10, 1, 5, 4, 4, 5, 4]
print(numbers.count(1))         # 2
print(numbers.count(3))         # 1
print(numbers.count(4))         # 4
print(numbers.count(7))         # 0

# note: count doesn't throw and error - it returns 0 if object is not in the collection

# index also works with strings - returns the first matching substring of the string

names = 'Karl Grace Clare Victor Antonina Trevor'
print(names.index('Clare'))     # 11
print(names.index('Trevor'))    # 33
# print(names.index('Chris'))     
# ValueError: substring not found


# Merging Collections
# zip - merge members of multiple iterables in a single list of tuples
# zip iterates thru 0 or more iterables in parallel and returns list of tuples
# Meaning zip takes all the elements in index 0 and places them in 1 tuple, takes the next element in index 1 and places them in second tuple, continues this process until it iterates completely through all the iterables.

# e.g
iterable1 = [1, 2, 3]
iterable2 = ('Kim', 'Leslie', 'Bertie')
iterable3 = [None, True, False]

zipped_iterables = zip(iterable1, iterable2, iterable3)
print(zipped_iterables) # <zip object at 0x1080502c0>
print(list(zipped_iterables))
print(list(zipped_iterables))
# [
#   (1, 'Kim', None),
#   (2, 'Leslie', True),
#   (3, 'Bertie', False),
#]

# zip returns a lazy sequence - similar to range - where explicit call to zipped list has to be made - print(list(zipped_iterable))

# zip's collection arguments are the same length but don't have to be
# to enforce identical lengths for collections add strict=True keyword argument when the function is called

# zip will raise an exception when strict=True argument is given

# when strict=True argument is missing, zip will stop after iterating through the shortest collection

result = zip(range(5, 10),
             range(1, 3),
             range(3, 7))
print(list(result)) 
# [(5, 1, 3), (6, 2, 4)]
print(list(result)) 

# zip returns what is known as an iterator
# iterators can only be used once
# if print(list(result)) is called again, the return value is an empty list

# For most Python functions and methods that return lazy sequences, they may be consumed only once.

# range objects are the exception to the rule


# Operations on Dictionaries
# 3 methods
# dict.keys, dict.values, dict.items

people_phones = {
    'Chris':    '111-2222',
    'Pete' :    '333-4444',
    'Clare':    '555-6666',
}

print(people_phones.keys())
# dict_keys(['Chris', 'Pete', 'Clare'])

print(people_phones.values())
# dict_values(['111-2222', '333-4444', '555-6666'])

print(people_phones.items())
# dict_items([('Chris', '111-2222'), ('Pete', '333-4444'), ('Clare', '555-6666')])

# the lists that are produced by above-mentioned objects are dictionary-view objects
# the dict is changed in any way, the dict lists are updated as well


people_phones = {
    'Chris': '111-2222',
    'Pete':  '333-4444',
    'Clare': '555-6666',
}

keys = people_phones.keys()
values = people_phones.values()

print(keys)
# dict_keys(['Chris', 'Pete', 'Clare'])
print(values)
# dict_values(['111-2222', '333-4444', '555-6666'])

people_phones['Max'] = '123-4567'
people_phones['Pete'] = '345-6789'
del people_phones['Chris']

print(keys)
# dict_keys(['Pete', 'Clare', 'Max'])
print(values)
# dict_values(['345-6789', '555-6666', '123-4567'])


# Operations for Mutable Sequences

# adding elements to mutable sequences
# append, insert, extend

# seq.append - adds a single object to the end of a list
numbers = [1, 2]
numbers.append(10) 
print(numbers)      # [1, 2, 10]

# seq.insert - inserts the element at a given index
# if the index is greater or equal to the sequence length, then it is appended to the sequence
# if the index is negative, it is counted from the end of the string

numbers = [1, 2]

numbers.insert(0, 8) # insert 8 before numbers[0]
print(numbers)  # [8, 1, 2]
numbers.insert(2, 6) # insert 6 before numbers[2]
print(numbers)  # [8, 1, 6, 2]
numbers.insert(100, 55) # insert 55 before numbers[100]
print(numbers)  # [8, 1, 6, 2, 55]
numbers.insert(-3, 33)  # insert 33 before 3rd number from the end
print(numbers) # [8, 1, 33, 6, 2, 55]

# seq.extend - appends the contents of an iterable sequence to the calling sequence

numbers = [1, 2]
numbers.extend([7, 8])
print(numbers)  # [1, 2, 7, 8]


# removing elements from a mutable sequence

# remove, pop, clear
# seq.remove looks for an object in a sequence
# if the object is found, the element is removed but if the item is not found it raises an error

my_list = [2, 4, 6, 8, 10]

my_list.remove(8)
print(my_list)  # [2, 4, 6, 10]

#my_list.remove(8)
print(my_list)  # ValueError: list.remove(x): x not in list

# seq.pop - removes and returns an indexed element
# if no index is given, then it removes and returns the last element
# if the index is out of range, it will raise an exception

my_list = [2, 4, 6, 8, 10]

print(my_list.pop(1))   # 4
print(my_list)          # [2, 6, 8, 10]

print(my_list.pop())    # 10
print(my_list)          # [2, 6, 8]

#print(my_list.pop(4))
# IndexError: pop index out of range


# seq.clear - clears all the elements in sequence

my_list = [2, 4, 6, 8, 10]
my_list.clear()
print(my_list)      # []


# Sorting Collections

# 2 methods
# sorted - sorts the elements and returns a new sorted list; original is unchanged
# list.sort - mutates the caller and returns a sorted list - faster and less memory intensive

# e.g
names = ('Grace', 'Clare', 'Allison', 'Trevor')
print(sorted(names))
# ['Allison', 'Clare', 'Grace', 'Trevor']

print(names)
# ('Grace', 'Clare', 'Allison', 'Trevor')

names = list(names)
print(names)
# 'Grace', 'Clare', 'Allison', 'Trevor']

print(names.sort())     # None
print(names)
# 'Allison', 'Clare', 'Grace', 'Trevor']

# by default, sort and sorted - perform ascending sort using < operator to compare elements from collection

# reverse sort - by using reverse=True
# e.g
names = ['Grace', 'Clare', 'Allison', 'Trevor']
print(sorted(names, reverse=True))
# ['Trevor', 'Grace', 'Clare', 'Allison']
print(names)

names.sort(reverse=True)
print(names)
# ['Trevor', 'Grace', 'Clare', 'Allison']

# pass in key=func to determine which values to sort

# e.g
words = ['abc', 'DEF', 'xyz', '123']
print(sorted(words))
# ['123', 'DEF', 'abc', 'xyz']

print(sorted(words, key=str.lower))
# ['123', 'abc', 'DEF', 'xyz']

# sort list of numeric-valued strings by passing key=int
numbers = ['1', '5', '100', '15', '534', '53']
numbers.sort()
print(numbers)
# ['1', '100', '15', '5', '53', '534']

numbers.sort(key=int)
print(numbers)
# '1', '5', '15', '53', '100', '534']



# reversing sequences and dictionaries
# 'reversed' function - reverse the order of elements in a seq or dict
# the return value is a lazy sequence
# - either iterate over the result
# - or expand it into a list or tuple

names = ('Grace', 'Clare', 'Allison', 'Trevor')
reversed_names = reversed(names)
print(reversed_names)
# <reversed object at 0x10ae53f70>

print(tuple(reversed(names))) # Req extra mem
# ('Trevor', 'Allison', 'Clare', 'Grace')

print(names)
# ('Grace', 'Clare', 'Allison', 'Trevor')

# also use list.reverse - but only when list needs to be reversed and the original is not needed

# note: use reversed when iteration over elements is needed
# use list.reverse if result needed is list or tuple
names = list(names)
print(names.reverse())
print(names)
# ['Trevor', 'Allison', 'Clare', 'Grace']

my_dict = {'abc': 1, 'xyz': 23, 'pqr': 0, 'jkl': 5}
reversed_dict = reversed(my_dict)
print(reversed_dict)
# <dict_reversekeyiterator object at 0x1080c0b80>

print(list(reversed_dict)) # extra memory
# ['jkl', 'pqr', 'xyz', 'abc']

# reversed function as looping aid
# e.g
names = ('Grace', 'Clare', 'Allison', 'Trevor')
for name in reversed(names):
    print(name)