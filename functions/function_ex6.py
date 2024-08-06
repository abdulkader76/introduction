# 6. What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yippeee')

# answer: the function is terminated with the return statement. So nothing will be printed out

# ls solution: This code also doesn't print anything. The return on line 3 terminates the function before it can print anything.