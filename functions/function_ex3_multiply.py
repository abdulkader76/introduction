# 3. Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

# write a function that multiplies two numbers

# Ask the user to enter two numbers
def get_number(num):
    number = input(f"Enter the {num} number: ")
    return float(number)

def multiply():
    first = get_number('first')
    second = get_number('second')
    return f"{first} * {second} = {first * second}"

# output the numbers and result as a simple equation
print(multiply())


# LS Solution:

# def multiply(left, right):
#     return left * right

# def get_number(prompt):
#     entry = input(prompt)
#     return float(entry)

# first_number = get_number('Enter the first number: ')
# second_number = get_number('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')
