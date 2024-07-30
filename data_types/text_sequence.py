# Examples of strings
'Hello!'
"He's pining for the fjords!"
'1969-07-20'
# f'{greeting}! My name is {my_name}'
r'\w+\d+'


greeting = 'hello'
for letter in greeting:
    print(letter)
    

# example of string literals
'Hi there'
"Monty Python's Flying Circus"

# Triple single quotes
'''King Arthur: "What is your name?"
Black Knight: None shall pass!"
King Arthur: "What is your quest?"
Black Knight: "I have no quarrel with you,
               but I mus cross this bridge."
'''

# Triple double quotes
"""Man: "Is this the right room for an argument?"
Other Man: "I've told you once."
Man: "No, you haven't"
"""

# example of accessing a character in a string
my_str = 'abc'

my_str[0]
# a

my_str[1]
# b

my_str[2]
# c

my_str[4]
# IndexError: string index out of range

# example of triple quote strings || escape

print("""My nickname is "Wolfy", What's yours?""")
print('My nickname is "Wolfy". What\'s yours?')
print("My nickname is \"Wolfy\". What's yours?")

# Example of double backslash / raw string literal
print("C:\\Users\\Xyzzy")
print(r"C:\Users\Xyzzy")

# Example of string literal f string
# f'5 plus 5 equals {5 + 5}'
# my_name = 'Karl'
# f'My name is {my_name}'

# Example of using braces within f string
# foo = 'hello'
#print(f'Use {{foo}} to embed a string: {foo}')

# Example of using f string with numbers
# print(f'{123456789:_}') # 123_456_789
# print(f'{123456789:,}') # 123,456,789

# Example of using f string for float
# print(f'{123456.7890123:_}')
# print(f'{123456.7890123:,}')

