# 7. What happens when you run the following code?
#    Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning ' + NAME)
print('Good Afternoon ' + NAME)
print('Good Evening ' + NAME)

# After the 3rd print statement, the NAME variable is re-assigned to 'Nina', and the output changes from 'Victor' to 'Nina' in the following 3 print statements.

# the variable is in uppercase which is usually used for constants and is considered poor practice to change the values of constants.
