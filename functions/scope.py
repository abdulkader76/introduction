# Example of scope #1
# def well_howdy(who):
#     greeting = 'Howdy'
#     print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting)
# NameError: name 'greeting' is not defined

# Example of scope # 2
# greeting = 'Salutations'

# def well_howdy(who):
#     greeting = 'Howdy'
#     print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting)

# Output
# Howdy, Angie
# Salutations

# Example of scope #3
# greeting = 'Salutations'

# def well_howdy(who):
#     print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting)

# Output
# Salutations, Angie
# Salutations

# Example of scope #4
# def scope_test():
#     if True:
#         foo = 'Hello'
#     else:
#         bar = 'Goodbye'
    
#     print(foo)
#     print(bar)

# scope_test()

# UnboundLocalError: cannot access local variable 'bar' where it is not associated with a value