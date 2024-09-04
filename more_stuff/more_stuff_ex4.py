# 4. Write a function called increment_counter that increments a counter variable every time it is called. You can test your code with the following:
counter = 0

def increment_counter():
    global counter
    counter += 1
    return counter

print(counter)

increment_counter()
print(counter)

increment_counter()
print(counter)

counter = 100
increment_counter()
print(counter)

# ls solution:
counter_1 = 0
def increment_counter_1():
    global counter
    counter += 1

# In this solution, we've first initialized a global counter variable to 0. Our increment_counter function simply incremenets this variable each time the function is called. However, since we're using counter += 1 in the code, we need to tell Python that counter, as used in increment_counter, is a global variable. We do this by including global counter in the function definition.