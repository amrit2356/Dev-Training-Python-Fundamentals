"""
Implementation of Decorators in Python

"""


def decorator_function(orig_func):
    def wrapper_function():
        print('Wrapper Executed this before: {}()'.format(orig_func.__name__))
        return orig_func()
    return wrapper_function

# Syntax 1 for creation of Decorators
# def display():
#     print('display function Ran')
# decorated_display = decorator_function(display)
# decorated_display()

# Syntax 2: using @ Symbol


@decorator_function
def display():
    print('display function Ran')


display()
