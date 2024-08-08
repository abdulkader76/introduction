# match/case Statement

# 'match' statement is similar to an 'if' statement - difference 'match' statement compares a single value while an 'if' statement compares multiple expressions

# 'match' statements are followed by a 'case'

# Example of match statement

value = 9

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _: # default code
        print('value is neither 5 nor 6')

# the match statement - evaluates the expression 'value' and compares its value with each case.

# If the case matches, then the code block will get executed.

# If the case doesn't match, then the code '_' will be executed by default.

# above example can be written with an 'if' statement

if (value == 5):
    print('value is 5')
elif (value == 6):
    print('value is 6')
else:
    print('value is neither 5 nor 6')

# example of using multiple values in a case statement - use | to separate values

value = 5

match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _: # default case
        print('value is not 1, 2, 3,  4, 5, or 6')
