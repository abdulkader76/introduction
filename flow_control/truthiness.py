# Truthiness
# truthy & falsy

# In conditional statements, such as if and while, the expressions e.g (4 == 4) do not produce a Boolean value.

# Instead, Python will evaluate the expression. If the expression evaluates to 'True', it is known as 'truthy'.

# Otherwise, it evaluates the expression to 'falsy' and Python will move on.

# conditionals only care about truthiness - any expression can be used as the condition

# built-in falsy values
# False, None
# numeric 0 values, (integers, floats, complex)
# empty strings ''
# empty collections [], (), {}, set(), frozenset() and range(0)
# custom data types can also define additional falsy values

# example of truthy value
value = 5
if value:
    print(f'{value} is truthy')
else:
    print(f'{value} is falsy')

# example of falsy value
value = 0
if value:
    print(f'{value} is truthy')
else:
    print(f'{value} is falsy')

# when a code returns an actual value, True or False, the term True or False can be used

# when Python evaluates an expression, then the expression is either truthy or falsy

# to keep it simple, you can say the expression is 'truthy' or 'falsy'


# Truthiness and Short-Circuit Evaluation

# and / or operators cause short-circuit evaluation

# these operators do not return True or False - instead they only look at the truthiness of the operands

# example of last operands being evaluated with 'and'
print(3 and 'foo')  # last evaluated op: 'foo'
print('foo' and 3)  # last evaluated op: 3
print(0 and 'foo')  # last evaluated op: 0
print('foo' and 0)  # last evaluated op: 0

# example of last operands being evaluated with 'or'
print(3 or 'foo')   # last evaluated op: 3
print('foo' or 3)   # last evaluated op: 'foo'
print(0 or 'foo')   # last evaluated op: 'foo'
print('foo' or 0)   # last evaluated op: 'foo'
print('' or 0)      # last evaluated op: 0
print(None or [])   # last evaluated op: []

# example of a logical expression that returns a non-Boolean object instead of a Boolean

foo = None
bar = 'qux'
is_ok = foo or bar

# in the above example, is_ok is set with 'qux'. using a string as boolean object could be a faux-pas when you write code

# if someone is reading your code, it will be difficult for them to debug your code and in some cases it may even be a mistake

# example of re-writing is_ok code:
if foo or bar:
    is_ok = True
else:
    is_ok = False

# is_ok is set to True or False based on the truthiness of foo or bar

# example of concise way of is_ok
is_ok = bool(foo or bar)



