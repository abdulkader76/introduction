# 14. Identify all of the identifiers on each line of the following code.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')


# answer:
# line 3 - multiply, left, right
# line 4 - left, right
# line 6 - get_num, prompt
# line 7 - prompt
# line 9 - first_number, get_num
# line 10 - second_number, get_num
# line 11 - product, multiply, first_number, second_number
# line 12 - first_number, second_number, product

# ls solution:
# Identifier 	Appears on these lines
# multiply 	        1, 9
# left 	            1, 2
# right 	        1, 2
# first_number 	    7, 9, 10
# second_number 	8, 9, 10
# get_num 	        4, 7, 8
# prompt 	        4, 5
# float 	        5
# input 	        5
# product 	        9, 10
# print 	        10