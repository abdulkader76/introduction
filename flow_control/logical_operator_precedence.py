# Logical Operator Precedence

# precedence rules for expressions with multiple operators and sub-expressions

# highest to lowest - from top to bottom
# '==', '!=', '<', '<=', '>', '>=' - Comparison
# not - Logical NOT
# and - Logical AND
# or - Logical OR

# e.g not x == y - x == y is evaluated first and the value is evaluated by NOT
# expression - not(x == y)

# when it comes to precedence, and takes higher precence than or, but 'short-circuit' adds more complexity to the equation

# determine which code prints what?
print(1 or 2 and 3) # 1
print(0 or 2 and 3) # 3
print(1 or 0 and 3) # 1
print(1 or 2 and 0) # 1
print(0 or 0 and 3) # 0
print(0 or 2 and 0) # 0
print(1 or 0 and 0) # 1
print(0 or 0 and 0) # 0

print(1 and 2 or 3) # 2
print(0 and 2 or 3) # 3
print(1 and 0 or 3) # 3
print(1 and 2 or 0) # 2
print(0 and 0 or 3) # 3
print(0 and 2 or 0) # 0
print(1 and 0 or 0) # 0
print(0 and 0 or 0) # 0

# when the expressions are evaluated, the output will be the last operand being evaluated before going to the next operator

# in short: avoid writing code in this manner
# use parentheses to explicitly indicate precedence

# e.g

# print((a and b) or (c and d)) - right way
# print(and b or c and d) - wrong way