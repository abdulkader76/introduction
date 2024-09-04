# Nested Functions

def foo():
    def bar():
        print('BAR')

foo()
bar()
# NameError: name 'bar' is not defined