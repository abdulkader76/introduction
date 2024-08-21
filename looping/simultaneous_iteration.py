# Simultaneous Iteration

# print full name of people - from 2 lists including forenames

forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

index = 0
while index < len(forenames):
    if index >= len(surnames):
        break 
    
    forename = forenames[index]
    surname = surnames[index]
    print(f'{forename} {surname}')
    
    index += 1

# using the above example with zip

forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

names = zip(forenames, surnames)
full_names = list(names)

for name in full_names:
    print(f'{name[0]} {name[1]}')


# ls example
forenames = ['Matthias', 'Noussair', 'Lenny', 'Joshua']
surnames = ['de Ligt', 'Mazraoui', 'Yoro', 'Zirkzee']

full_names = zip(forenames, surnames)
for forename, surname in full_names:
    print(f'{forename} {surname}')