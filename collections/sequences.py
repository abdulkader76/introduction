# Sequences

# there 3 categories of collections:
# sequences
# maps
# sets

# a sequence is any type that maintains an ordered of collection of objects that can be indexed by whole numbers

# an ordered collection is a collection of objects that are organized in a sequence

# an indexed sequence is a way to identify object in that collection in order to access/modify that object

# built-in sequences - range, list, tuple

# list seq [0]  [1]  [2]
letters = ['a', 'b', 'c']
print(letters[0])       # 'a'
print(letters[1])       # 'b'
print(letters[2])       # 'c'

# when a sequence can contain multi-ple objects, incl. other sequences - heterogenous - lists, tuples

# e.g
my_list = [
    'May',
    2.99,
    {None, True, False},
    [1, 2, 3],
]

# ranges - homogenous - only contain integers

# Strings
# strings - homogenous - strings only have characters
# characters aren't distinct objects; strings of length 1
# string's individual characters are separate strings until you reference them
# strings aren't actual collections since characters insides strings aren't objects

# e.g string - bullet point 3



# strings are homogenous
# e.g 'example132332' - all characters
# characters are not distinct objects; they are strings of length 1
# e.g 'e', 'x', 'a', 'm',....
# string's individual characters are not separate strings until a reference is made

# example 1
letters = ['a', 'b', 'θ', 'd', 'e']
char = letters[2]
print(char is letters[2])

# example 2
letters = 'abθde'
char = letters[2]
print(char is letters[2])

# the first example, char is assigned theta in the letters list. In this reference, both char and letters[2] are referencing the same object

# the second exaple, char is assigned theta from the string but even though the values are the same, they reference two different objects
# e.g id(char)          # 4493830704
# e.g id(letters[2])    # 4492969776

# strings are not collections as the characters in a string aren't objects

