# default parameters

# def say(text='hello'):
#     print(text + '!')

# say('Howdy')        # Howdy!
# say()               # hello!

# invoke a fn without passing in any args by initializing the fn's parameters with default val

# example of default parameter error
# def say(msg1, msg2, msg3='dummy message', msg4):
#     pass

# SyntaxError: non-default arg follows default argument

# def say(msg1,
#         msg2,
#         msg3="dummy message",
#         msg4="omitted message"):
#     print(msg1)
#     print(msg2)
#     print(msg3)
#     print(msg4)

# say('a', 'b', 'c', 'd')
# a
# b
# c
# d

# say('a', 'b', 'c')
# a
# b
# c
# omitted message

# say('a', 'b')
# a
# b
# dummy message
# omitted message

# say('a', 'b', 'd')
# a
# b
# d                 # expecting dummy message
# omitted message   # expecting 'd'
