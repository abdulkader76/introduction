# Set Comprehensions

# same as dictionary except for expression
# only has one expression

# { expression for element in iterable 
#                   if condition }

# basic example of set comprehension
squares = { 
    number * number 
    for number in range(1, 6)
    }

print(squares)
# {1, 4, 9, 16, 25}

# dicts and sets are identical comprehensions
# other than the expression