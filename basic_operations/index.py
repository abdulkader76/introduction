# Indexing and Key access

# my_str = 'abc'
# print(my_str[0])                  # 'a'
# print(my_str[1])                  # 'b'
# print(my_str[2])                  # 'c'
# print(my_str[3]) 
# IndexError: string index out of range

# my_range = range(5, 8)
# print(my_range[0])                # 5
# print(my_range[1])                # 6
# print(my_range[2])                # 7
# print(my_range[3])
# IndexError: range object out of range

# my_list = [4, 5, 6]
# print(my_list[0])                 # 4
# print(my_list[1])                 # 5
# print(my_list[2])                 # 6
# print(my_list[3])
# IndexError: list index out of range

# tup = (8, 9, 10)
# print(tup[0])                     # 8
# print(tup[1])                     # 9
# print(tup[2])                     # 10
# print(tup[3])
# IndexError: tuple index out of range

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict['a'])               # 1
# print(my_dict['b'])               # 2
# print(my_dict['c'])               # 3
# print(my_dict['d'])               # KeyError


# Using [] to update elements

# my_list = [1, 2, 3, 4]
# my_list[2] = 6            
# print(my_list)                    # [1, 2, 6, 4]
# my_list[4] = 10
# IndexError: list assignment index out of range

# my_dict = {
    # 'dog': 'barks',
    # 'cat': 'meows',
    # 'pig': 'oinks',
# }

# my_dict['pig'] = 'snorts'
# print(my_dict)

# {
#     'dog': 'barks',
#     'cat': 'meows',
#     'pig': 'snorts',
# }

# use [] to add new elements in a dict
 
# my_dict['fish'] = 'glub glub'
# print(my_dict)

# {
#     'dog': 'barks',
#     'cat': 'meows',
#     'pig': 'snorts',
#     'fish': 'glub glub',
# }