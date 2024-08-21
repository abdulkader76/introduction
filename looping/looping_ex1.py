# 1. The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)


# code is missing one step: counter += 1
# while loop will keep going as counter value remains at 0, thus below 5

# ls solution
# The problem occurs in the loop body. We never increment counter, so counter < 5 always returns a truthy value.