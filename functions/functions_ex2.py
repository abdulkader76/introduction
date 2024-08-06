# 2. Take a look at this code snippet:

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# What does this program print? Why?

# Ans: 
# the code will print - 'bar'
# the set_foo() is called but there is no return statement. The variable foo will be initialized with 'qux' and the function will terminate with an implicit return of None
# Nothing will be output when set_foo() function is called

# LS solution: The program prints bar since the assignment on line 4 creates a new variable that is local to the function. That is, the foo variable on line 4 shadows the foo variable on line 1, so line 4 doesn't change the value of foo from line 1.