# Logical Operators

# not
# returns inverse of operand
# True - False, False - True

print(not True)     # False
print(not False)    # True
print(not(4 == 4))  # False
print(not(4 != 4))  # True

# and & or
# 'and' returns True when both operands are True and False when both or either one is False

print((4 == 4) and (7 == 7))    # True
print((4 == 4) and (7 == 3))    # False
print((4 == 9) and (7 == 7))    # False
print((4 == 9) and (7 == 3))    # False


# 'or' returns True when both or either operand is True and False when both operands are False

print((4 == 4) or (7 == 7))     # True
print((4 == 4) or (7 == 3))     # True
print((4 == 9) or (7 == 7))     # True
print((4 == 9) or (7 == 3))     # False

# Always use parentheses unless the comparison is with a single identifier or literal