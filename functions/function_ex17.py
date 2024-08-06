def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# 17. Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?

# answer:
# function names - say, print, input, max
# method names - upper(), lower()
# built-in functions - print, input, max


# ls solution:
# If you identified all the method and built-in function names as function names, that's an acceptable answer as well: all methods are functions, and built-in functions are just functions that are, well, built-in.

