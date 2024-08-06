# 11. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# answer:
# the output will be: 42, 3, 2
# Only one argument is passed into the foo function so python will use the default values from the function definition

# ls solution: 
# Here, we've defined foo with three parameters, with the second and third parameters having a default value. We've passed the function one argument, so Python uses the default value for the last two parameters.