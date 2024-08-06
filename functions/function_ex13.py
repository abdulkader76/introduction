# 13. Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# answer:
# python will raise an error for the function declaration - when a parameter has default value, the following parameters will also have to be declared with a default value
# the function will not run when foo(42) is called

# ls solution
# Here, we've defined foo with three parameters, with the second parameter having a default value. This is an error, however. Once Python sees a positional parameter with a default value, all subsequent parameters must have default values.