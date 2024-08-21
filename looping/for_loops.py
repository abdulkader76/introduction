# for loops

# for element in collection:
    # loop body: do something with the element

# e.g changing the names to uppercase
names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    uppercase_name = name.upper()
    upper_names.append(uppercase_name)
    # Deleted: index += 1

print(upper_names)
# 'CHRIS', 'MAX', 'KARIS', 'VICTOR']

# chars.py
for char in 'Launch School':
    print(char)

# L
# a
# u
# n
# c
# h
#      # empty space
# S
# c
# h
# o
# o
# l

# print words instead of char - use split
for word in 'Launch School'.split():
    print(word)

# Launch
# School

# use for loops with sets and dicts

# looping over a set
my_set = {1000, 2000, 3000, 4000, 5000}
for member in my_set:
    print(member)

# output may not be in sequence
# 4000
# 2000
# 5000
# 3000
# 1000

# Looping over a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

# a
# b
# c

# Looping over a dictionary and getting values
my_dict = {'a': 1, 'b': 2, 'c': 3}
for value in my_dict.values():
    print(value)

# Looping over dictionary - printing pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
for item in my_dict.items():
    print(item)


# printing key-values pairs - use tuple unpacking
my_dict = {'a': 1, 'b': 2, 'c': 3}
for (key, value) in my_dict.items():
    print(f"{key} = {value}")

# printing key-values - use tuple unpacking
# without parentheses
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f'{key} = {value}')


# Nested Loops
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

print(deck)
