# Indexing
# to access or alter any element by using whole number is called indexing

seq = ('a', 'b', 'c')
print(seq[0])       # 'a' (1st element)
print(seq[1])       # 'b' (2nd element)
print(seq[2])       # 'c' (3rd element)
#print(seq[3])       # IndexError: tupel index out of range

# index of last element is one less than the length of sequence

# seq = ('a', 'b', 'c')
# if len(seq) > 3:
#     print(seq[3])

# access the last element of sequence
seq = ('a', 'b', 'c')
last_index = len(seq) - 1
print(seq[last_index])      # 'c'

# use negative indexes 
seq = ('a', 'b', 'c')
print(seq[-1])          # 'c'
print(seq[-2])          # 'b'
print(seq[-3])          # 'a'

# change the element of a sequence (if the object is mutable)
seq = ['a', 'b', 'c']
seq[1] = 'B'
print(seq)          # ['a', 'B', 'c']

# by re-assigning the seq[1], the list is mutated

