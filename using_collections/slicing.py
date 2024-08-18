# Slicing
# e.g seq = 'abcdefghi'
# to extract a portion of seq string, use slicing augmentation with indexing syntax
# e.g seq[3:7] - 'defg'
# 3 is index starting point 
# 7 is the stop point - last character will 7 - 1 at index 6
# so the seq[start:stop] - start index and stop - 1 index
# sequences can also be indexed backwards using negative values
# also use [start:stop:step] - where the character is jumped every step-th, similar to ranges

seq = 'abcdefghi'
#      012345678
print(seq[3:7])         # 'defg'
print(seq[-6:-2])       # 'defg'
print(seq[2:8:2])       # 'ceg'
# [start:stop] values the same; empty str
print(repr(seq[3:3]))   # ''

# seq[:] returns duplicate sequence - same as [0: len(seq)]
print(seq[:])           # 'abcdefghi'

# returns reversed copy of sequence - seq[::-1] same as seq.reverse()
# seq[::-1] - a new reversed sequence
# seq.reverse() - mutates original; easier to read but mutation should be intentional
print(seq[::-1])        # 'ihgfedcba'

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(seq[3:7])         # [4, 5, 6, 7]
print(seq[-6:-2])       # [4, 5, 6, 7]
print(seq[2:8:2])       # [3, 5, 7]

# returns a empty list; start, stop values same
print(seq[3:3])         # []

# returns a new list, a duplicate copy
print(seq[:])           # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns a new list that is reversed
# same as seq.reverse() but is a copy instead of mutating the original
print(seq[::-1])        # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# seq_dup is assigned the seq[:] but example of shallow copy
seq = [[1, 2], [3, 4]]
seq_dup = seq[:]
print(seq[0] is seq_dup[0])     # True