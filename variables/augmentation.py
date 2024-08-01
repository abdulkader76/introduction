# Augmented Assignments

# e.g
# foo = 42              # foo is 42
# foo -= 2              # foo is 40
# foo *= 3              # foo is 120
# foo += 5              # foo is 125
# foo //= 25            # foo is 5
# foo /= 2              # foo is 2.5
# foo **= 3             # foo is 15.625
# print(foo)            # 15.625

# Augmented assg works with string 
# concatenation & repetition
# bar = 'xyz'           # bar is 'xyz'
# bar += 'abc'          # bar is 'xyzabc'
# bar *= 2              # bar is 'xyzabcxyzabc'
# print(bar)            # 'xyzabcxyzabc'

# e.g. with lists
# bar = [1, 2, 3]       # bar is [1, 2, 3]
# bar += [4, 5]         # bar is [1, 2, 3, 4, 5]
# print(bar)            # [1, 2, 3, 4, 5]

# e.g with sets
# bar = {1, 2, 3}       # bar is {1, 2, 3}
# bar |= {2, 3, 4, 5}   # | performs set union
                        # bar is {1, 2, 3, 4, 5}
# bar -= {2, 4}         # bar is {1, 3, 5}
# print(bar)            # {1, 3, 5}

# augmented assgn is a statement, not an expression

# def foo(bar):
#   print(bar)

# a = 3
# foo(a *= 2)
# SyntaxError: invalid syntax

# def foo():
    # a = 3
    # return a *= 2
# SyntaxError: invalid syntax

