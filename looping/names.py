# iterate over a list of names and create a new list that contains the names in uppercase

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):
    uppercase_name = names[index].upper()
    upper_names.append(uppercase_name)
    index += 1

print(upper_names)
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']