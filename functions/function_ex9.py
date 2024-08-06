# 9. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# answer:
# the output:   42
#               3.141592
#               2.718
# the foo function call will print the above
# the 2nd & 3rd parameters have default values but they will only be initialized if the 2nd and 3rd args are not passed into the foo function

# ls solution:
# Here, we've defined foo with three parameters, with the second and third parameters having default values. However, we've passed all three arguments to the function, so Python ignores the default values.