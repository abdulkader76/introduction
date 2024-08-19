# 11. Without running the following code, determine what each line should print.

print('johnson' in 'Joe Johnson') # False
print('sen' not in 'Joe Johnson') # True
print('Joe J' in 'Joe Johnson') # True
print(5 in range(5))    # False
print(5 in range(6))    # True
print(5 not in range(5, 10))    # False
print(0 in range(10, 0, -1))    # False
print(4 in {6, 5, 4, 3, 2, 1})  # True
print({1, 2, 3} in {1, 2, 3})   # False
print({3, 2} in {1, frozenset({2, 3})}) # True


# ls solution
print('johnson' in 'Joe Johnson')      # False
print('sen' not in 'Joe Johnson')      # True
print('Joe J' in 'Joe Johnson')        # True
print(5 in range(5))                   # False
print(5 in range(6))                   # True
print(5 not in range(5, 10))           # False
print(0 in range(10, 0, -1))           # False
print(4 in {6, 5, 4, 3, 2, 1})         # True
print({1, 2, 3} in {1, 2, 3})          # False
print({3, 2} in {1, frozenset({2, 3})}) # True


# Line 1: in with strings is case sensitive.
# Line 4: range(5) does not include 5; it ranges from 0 to 4.
# Line 7: range(10, 0, -1) does not include 0; it ranges from 10 to 1.
# Line 9: in with sets only checks whether a specific value is in the set.
# Line 10: {3, 2} and frozenset({2, 3}) are considered equal sets.
