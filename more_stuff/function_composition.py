# Function Composition

# composition - function call used as amn argument in another function call - the return value is used as an argument

# e.g
print(list(range(3, 17, 4)))
# [3, 7, 11, 15]

# e.g
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

sum = add(20, 45)
print(sum)

difference = subtract(80, 10)
print(difference)

# e.g use func comp for above example
print(add(20, 45))
print(subtract(80, 10))

# e.g more complex example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def times(num1, num2):
    return num1 * num2

print(times(add(20, 45), subtract(80, 10)))
# 4550 == ((20 + 45), (80 - 10))

# e.g with verbose code
total = add(20, 45)
difference = subtract(80, 10)
result = times(total, difference)
print(result)


# e.g 
def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

def sum(num1, num2):
    return num1 + num2

times = multiply(20, 10)
divide = division(400, 20)
total = int(sum(times, divide))
print(total)
