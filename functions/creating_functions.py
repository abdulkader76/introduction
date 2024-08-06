# example of function
# def say():
#     print("Output from say")

# print('First')
# say()
# print('Last')

"""
Triple quoted string at the beginning of a function - documentation comment
"""
def say():
    """
    The say function prints "Hi!"
    """
    print("Hi!")

print('-' * 60)
print(say.__doc__)
print('-' * 60)
help(say)