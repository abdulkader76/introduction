# 10. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# answer:
# the code will print 42, 3.141592, 2
# the third argument is missing when the function is called so python will take the default value

# ls solution:
# Here, we've defined foo with three parameters, with the second and third parameters having default values. We've passed the function two arguments, so Python uses the default value for the last argument.