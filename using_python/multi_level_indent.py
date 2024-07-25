# Example of mulitple level of indentation

# avoid using more than 2 levels

if value <= 10:
    print('value <= 10')
    if value >= 5:
        print("value >= 5")
    else:
        print("value < 5")
else:
    print("value > 10")