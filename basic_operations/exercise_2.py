# This question may be a little challenging if your math skills are rusty. Don't be afraid to take advantage of the hints. Try your best to solve the problem, but don't feel compelled to complete it if you become frustrated.

# Use the REPL and the arithmetic operators to extract the individual digits of 4936:


    # One place is 6.
    # Tens place is 3.
    # Hundreds place is 9.
    # Thousands place is 4.

# Each digit may require multiple Python statements.

x = 4936 - 4000 - 900 - 30
print(x)

y = (4936 - 4000 - 900 - 6) // 10
print(y)

z = (4936 - 4000 - 30 - 6) // 100
print(z)

zz = (4936 - 900 - 30 - 6) // 1000
print(zz)

# Solution
number = 4936
ones = number % 10
print(ones)

number = number // 10
tens = number % 10
print(tens)

number = number // 10
hundreds = number % 10
print(hundreds)

thousands = number // 10
print(number)