# Determining Types

# print(type(1))            # <class 'int'>
# print(type(3.14))         # <class 'float'>
# print(type(True))         # <class 'bool'>
# print(type('abc'))        # <class 'str'>
# print(type([1, 2, 3]))    # <class 'list'>
# print(type(None))         # <class 'NoneType'>

# foo = 42                  
# print(type(foo))          # <class 'int'>

# add __name__ if you just want the class name
# print(type('abc').__name__)       # str
# print(type(False).__name__)       # bool
# print(type([]).__name__)          # list


# use type with is operator

# print(type('abc') is str)         # True
# print(type('abc') is int)         # False
# print(type(False) is bool)        # True
# print(type([]) is list)           # True
# print(type([]) is set)            # False


# using isinstance function which takes inheritance into account

# print(isinstance('abc', str))     # True
# print(isinstance([], set))        # False

# class A:
#   pass

# class B(A):
#   pass

# b = B()

# print(type(b).__name__)           # B
# print(type(b) is B)               # True
# print(type(b) is A)               # False

# print(isinstance(b, B))           # True
# print(isinstance(b, A))           # True (b is instance of A and B) 