# 1. What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)


# Ans:
# Python will raise an error
# the variable is only defined within the function scope
# NameError: name 'foo' is not defined
