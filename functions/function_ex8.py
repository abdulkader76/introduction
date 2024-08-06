# 8. Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3,141592, 2,718)

# answer:
# python will raise an error: too many arguments for function foo
# foo is declared with 2 parameters, but when the function is called, there are 3 arguments being passed into the foo function

# ls solution:
# TypeError: foo() takes 2 positional arguments, but 3 were given

# We've defined foo with two parameters. However, we've passed the function three arguments. This is an error.

