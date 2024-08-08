value = int(input('Enter a number: '))

# example 1
if value == 3:
    print('value is 3')

# example 2
if value == 3:
    print('value is 3')
else:
    print('value is not 3')

# example 3
if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')

# example 4
if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')

# example 5
if value == 3:
    print('value is 3')
    print('value is an odd number')
    print('value is a prime number')
elif value == 4:
    print('value is 4')
    print('value is an even number')
    print('value is NOT a prime number')
elif value == 9:
    print('value is 9')
    print('value is an odd number')
    print('value is NOT a prime number')
else:
    print('value is something else')


# example 6
if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
elif value == 9:
    pass # adding a comment on pass is good practice
else:
    print('value is something else')

# example 7
if value == 1:
    print('value is one') # block will end here
print('the value is odd') # outdented print function will execute even if the if statement is False
