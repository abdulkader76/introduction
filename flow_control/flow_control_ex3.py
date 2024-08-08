# 3. Without running the following code, what does it print? Why

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

# The first function call prints 'Product2' as the case matches the serial

# The second function call prints 'Product not found' as the case doesn't match. The input variable in this case is an integer 142 and its comparison with '142' will evaluate to falsy.


# launchschool solution
# Product2
# Product not found!
# The first call to bar_code_scanner prints Product2 since the first case that matches '113' is the one on line 5. The second call prints Product not found! since the numeric value 142 doesn't match any of the case statements with string arguments. Instead, it matches the _ "default" case.
