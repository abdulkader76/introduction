# Dictionary Comprehensions

# create new dictionaries
# use curly braces 
# expression is a 'key: value' pair

# e.g
# { key: value for element in iterable
#                   if condition }

# basic e.g dict comprehension
squares = { 
    f'{number}-squared': number * number
    for number in range(6)
    }

print(squares)
# {
    # '0-squared': 0, 
    # '1-squared': 1, 
    # '2-squared': 4, 
    # '3-squared': 9, 
    # '4-squared': 16, 
    # '5-squared': 25
# }
