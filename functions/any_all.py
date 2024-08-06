# collection1 = [False, False, False]
# collection2 = (False, True, False)
# collection3 = {True, True, True}

# print(any(collection1))   # False
# print(any(collection2))   # True
# print(any(collection3))   # True
# print(any(collection4))   # False

# print(all(collection1))   # False
# print(all(collection2))   # False
# print(all(collection3))   # True
# print(all([]))            # True

# use list comprehension 
# numbers = [2, 5, 8, 10, 13]
# print([number % 2 == 0 for number in  numbers])

# numbers = [2, 5, 8, 10, 13]
# print(any([number % 2 == 0 for number in numbers]))   # True
# print(all([number % 2 == 0 for number in numbers]))   # False       

# numbers = [5, 13]
# print(any([number % 2 == 0 for number in numbers]))   # False
# print(all([number % 2 == 0 for number in numbers]))   # False

# numbers = [2, 8, 10]
# print(any([number % 2 == 0 for number in numbers]))   # True
# print(all([number % 2 == 0 for number in numbers]))   # True

