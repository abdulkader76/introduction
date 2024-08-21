# 9. Write a function that computes and returns the factorial of a number by using a for or while loop. The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:


def factorial(numbers):
    total = 1
    for number in range(1, numbers + 1):
        total *= number
    
    return total

print(factorial(5))

# ls solution
# using a while loop
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1

    return result

# using a for loop
def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number

    return result

