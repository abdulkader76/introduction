# 4. Refactor this statement to use a regular if statement

# return ('bar' if foo() else qux())

if foo():
   return 'bar'
else:
   return qux()

# launchschool solution
# same as above

# Ternaries are most useful when both result values are given by simple expressions; anything more complicated than calling a function or accessing a variable or literal value can lead to unreadable code. Our original code is an excellent example of using the ternary expression; the refactoring merely demonstrates how the ternary works.