# 7. Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# ans
# python will raise a missing argument error
# function foo takes 2 args, only one is defined

# ls solution:
# TypeError: foo() missing 1 required positional
# argument: 'qux'

# We've defined foo with two parameters. However, we've only passed it one argument. This is an error.

