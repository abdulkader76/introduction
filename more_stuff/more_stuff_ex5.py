# 5. On reflection, we've decided that we don't want to rely on using a global variable in the code we wrote in the previous example. To fix this, we're going to nest the code from the previous example into an outer function:


def all_actions():
    counter = 0

    def increment_counter():
        # global counter
        nonlocal counter
        counter += 1

    print(counter)

    increment_counter()
    print(counter)

    increment_counter()
    print(counter)

    counter = 100
    increment_counter()
    print(counter)


all_actions()

# There's a bug in this code. Identify the bug, and fix it.

# bug in line 8 - # NameError: name 'counter' is not defined

# fix - change global counter to nonlocal counter

# ls solution
# The bug in this code is that the global keyword only works with global variables. If you're in a nested function and want to reassign a variable that is in the outer function, you have to use the nonlocal keyword instead:

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()