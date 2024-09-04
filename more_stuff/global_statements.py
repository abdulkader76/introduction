# the global and nonlocal statements

# global & nonlocal

# e.g var defined outside of a function is available within a function

greeting = 'Salutations'

def well_howdy(who):
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)

greeting2 = 'Salutations'

def well_howdy2(who):
    greeting2 = 'Howdy'
    print(f'{greeting2}, {who}')

well_howdy2('Angie')
print(greeting2)

# e.g of using global

greeting3 = 'Salutations'

def well_howdy3(who):
    global greeting3
    greeting3 = 'Howdy'
    print(f'{greeting3}, {who}')

print(greeting3)
well_howdy3('Angie')
print(greeting3)

# global variable
# a = 3

# def foo():
#     global a
#     a = 5
#     print(a)

# print(a)
# foo()
# print(a)


# e.g nonlocal 

def outer():
    def inner1():
        def inner2():
            foo = 3
            print(f"inner2 -> {foo} with id {id(foo)}")

        foo = 2
        inner2()
        print(f"inner1 -> {foo} with id {id(foo)}")

    foo = 1
    inner1()
    print(f"outer -> {foo} with id {id(foo)}")

outer()

# e.g of using global in nested functions
def outer_a():
    def inner1_a():
        def inner2_a():
            global foo
            foo = 3
            print(f"inner2_a -> {foo} with id {id(foo)}")

        foo = 2
        inner2_a()
        print(f"inner1_a -> {foo} with id {id(foo)}")

    foo = 1
    inner1_a()
    print(f"outer_a -> {foo} with id {id(foo)}")

outer_a()
print(f"globa_a -> {foo} with id {id(foo)}")

# e.g using nonlocal in nested functions

def outer_b():
    def inner1_b():
        def inner2_b():
            nonlocal foo
            foo = 3
            print(f"inner2_b -> {foo} with id {id(foo)}")

        nonlocal foo
        foo = 2
        inner2_b()
        print(f"inner1_b -> {foo} with id {id(foo)}")

    foo = 1
    inner1_b()
    print(f"outer_b -> {foo} with id {id(foo)}")

outer_b()
# print(f"global_b -> {foo} with id {id(foo)}")

def outer_loop():
    def inner_loop():
        
        nonlocal foo
        foo = 'inner'
        print(f"inner_loop -> {foo} id {id(foo)}")
    
    foo = 'outer'
    inner_loop()
    print(f"outer_loop -> {foo} id {id(foo)}")

outer_loop()

