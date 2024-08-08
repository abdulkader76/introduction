# 2. Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.

# Write a function even_or_odd
# using 'if' statement
def even_or_odd(number):
    # if it's even, it should print even
    if (number % 2 == 0):
        print('even')
    # if it's odd, it should print odd
    else:
        print('odd')

even_or_odd(2)
even_or_odd(13)
even_or_odd(12233445558)

# using ternary expression
def even_or_odd2(number):
    print('even' if number % 2 == 0 else 'odd')

even_or_odd2(12244)
even_or_odd2(5)
even_or_odd2(1249)


# launchschool solution

# solution 1
# def even_or_odd(number):
#     if number % 2 == 0:
#         print('even')
#     else:
#         print('odd')

# solution 2
# def even_or_odd(number):
#     print('even' if number % 2 == 0 else 'odd')
