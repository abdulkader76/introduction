# 4. This is a 3-part question. Consider the following dictionary:

pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}

# Part 1: Write some code to print Bark by accessing the element associated with the key Dog. 

for name in pets:
    if name == 'Dog':
        print(pets[name])

# Part 2: Write some code to print None when you try to print the value associated with the non-existent key, Lizard. 

def sound(name):
    if name in pets:
        print(pets[name])
    else:
        print('None')

sound('Dog')
sound('Lizard')

# Part 3: Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard. 

def sound(name):
    if name in pets:
        print(pets[name])
    else:
        print('<silence>')

sound('Dog')
sound('Lizard')


# ls solution

# Part1
print(pets['Dog'])
# Part2
print(pets.get('Lizard'))
# Part3
print(pets.get('Lizard', '<silence>'))
