# 6. Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of my_list. In this problem, you should write code that creates a new list with one element for each number in my_list. If the original number is an even, then the corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

even_odd = []
for number in my_list:
    if number % 2 == 0:
        even_odd.append('even')
    else:
        even_odd.append('odd')

print(even_odd)


result = [ 'even' if number % 2 == 0 else 'odd' for number in my_list]


# ls solution
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

result = []
for number in my_list:
    if number % 2 == 0:
        result.append('even')
    else:
        result.append('odd')

print(result)


# list comprehension
# using ternary operation - less readability
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

result = [ 
    'even' if number % 2 == 0 else 'odd' 
    for number in my_list ]
print(result)


# solution 3 - use helper function
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'

result = [ odd_or_even(number)
           for number in my_list ]
print(result)