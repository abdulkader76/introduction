# Arguments & Parameters

# example_1

# print('hello')
# print('hi')
# print('how do you do')
# print('Quite all right')

# duplicate print call many times

# example_2

def say(text):
    print(text)

say('hello')
say('hi')
say('how do you do')
say('Quite all right')

# extracted logic for displaying text
# to modify output, just modify it in one place

# if fns need to acesss outside data, pass the data thru arguments

# args not needed if fns no need of outside data

# (text) - like a cupholder - text is a placeholder (parameter) for data (arguments) to be passed into the function when it is called

# say('hello') passes argument 'hello' to the say function - value 'hello' assigned to text parameter

# names in () in fn def - parameters
# parameters placeholder for potential args
# args are values assigned to parameters

# fn names & param - variable names
# param - local variables
# fn name - local or global depending on their definition in the program; maybe local or global

# param - spoken of as declarations
# being used to introduce names as local var into a fn but no value until the fn is called
# declare variable names

# distinction between parameters & arguments
# args - obj pass into fn
# param - placeholder for obj to be pass into fn

# use meaningful, explicit names - fns & params
# e.g say(text) - alt: sentence, message

# when say fn is called, a value should be given the arg - assign to text param
# fn can use the value as it pleases - even ignore the value
# scope of fn param is within the fn
# e.g text is only accessible within say fn


# example_4
# fn def - any number of param
# fn call - any number of args

# def add(left, right):
#     sum = left + right
#     return sum

# sum = add(3, 6)

# say('hello') - 'hello' was passed as arg
# 'hello' was assigned to text param

# fn benefit - makes changes in one location
# def say(text):
#     print('==> ' + text)

# say('hello')            # ==> hello
# say('hi')               # ==> hi
# say('how are you')      # ==> how are you
# say("I'm fine")         # ==> I'm fine


