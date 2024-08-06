def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# 16. In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

# function names
# multiply - line 1, 9
# get_num - line 4, 7, 8
# float - line 5
# input - line 5
# print - line 10

# parameters
# left, right - line 1, 2
# prompt - line 3, 4


# ls solution:

# Function names:
#     multiply: defined on line 1, used on line 9.
#     get_num: defined on line 4, used on lines 7 and 8.
#     float: built-in function used on line 5.
#     input: built-in function used on line 5.
#     print: built-in function used on line 10.
# Parameters:
#     left and right are defined on line 1 and then used on line 2.
#     prompt is defined on line 4 and then used on line 5.

# Note that left and right are defined as parameters for the multiply function on line 1. We reference those parameters on line 2, but usually speak of them as local variables instead of parameters. For this exercise, it's okay if you said that left and right are present on line 2. It's also okay if you omitted it.

# Likewise, prompt is defined as a parameter for the get_num function on line 4, but used as a local variable on line 5.
