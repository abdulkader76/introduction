# 12. Without running the following code, what do you it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# answer:
# python will raise an error for missing arguments; the foo function has default values for 2nd & 3rd parameters but when the function is called, there has to be at least 1 argument passed into it

# ls solution:
# Here, we've defined foo with three parameters, with the second and third parameters having default values. We haven't passed the function any arguments. That's an error, though - the first parameter has no default value.