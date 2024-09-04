# Function Definition Order

def top():
    bottom()

def bottom():
    print('Reached the bottom')

top()


# call function before function definition

# top()

# def top():
#     bottom()

# def bottom():
#     print("Reached the bottom")
# NameError: name 'top' is not defined
