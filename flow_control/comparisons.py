# Comparisons

# comparison operators - return True or False
# e.g x == y
# == operator
# x, y operands
# the x == y uses the '==' operator with 2 operands

# equality operator '=='
# returns True when operands have equal values, False otherwise

print(5 == 5)           # True
print(5 == 4)           # False

print('abc' == 'abc')   # True
print('abc' == 'abcd')  # False

print(5 == '5')         # False

print([1, 2, 3] == [1, 2, 3])   # True
print([1, 2, 3] == [3, 2, 1])   # False

print(5 == float(5))    # True

big_num  = 12345678901234567
print(float(big_num) == big_num)    # False

# example case sensitive
print('abc' == 'aBc')   # False
print('abc'.lower() == 'aBc'.lower()) # True
print('abc'.upper() == 'aBc'.upper()) # True

# example using casefold
'straße'.casefold() == 'strasse'.casefold()
'abc'.casefold() == 'aBc'.casefold

# casefold is only needed with non-US characters but it is best practice to use instead of upper() and lower()


# != - inequality operator
# inverse of '=='
# returns True when False; vice versa

print(5 != 5)           # False
print(5 != 4)           # True
print('abc' != 'abc')   # False
print('abc' != 'aBc')   # True
print(5 != '5')         # True

# < and <= - less than operator
# left operand value less than right operand
print(4 < 5)    # True
print(5 < 4)    # False
print(5 < 5)    # False

print(4 <= 5)   # True
print(5 <= 4)   # False
print(5 <= 5)   # True

print('4' < '5')    # True
print('5' < '4')    # False
print('5' < '5')    # False

print('42' < '402') # False
print('42' < '420') # True
print('420' < '42') # False

# when doing string comparisons, python will compare the strings from left to right, and if there is no difference, then the length of the string is compared before a True or False value is returned


# > & >=    # greater & greater than
# left operand value greater than right operand

print(4 > 5)    # False
print(5 > 4)    # True
print(5 > 5)    # False

print(4 >= 5)   # False
print(5 >= 4)   # True
print(5 >= 5)   # True

print('4' > '5')    # False
print('5' > '4')    # True
print('5' > '5')    # False

print('42' > '402') # True
print('42' > '420') # False
print('420' > '42') # True
