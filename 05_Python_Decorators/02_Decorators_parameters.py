"""
Implementation of Decorators on Functions having Parameters in Python

"""
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper Executed this before: {}()'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    
    return wrapper_function

#Syntax 1 for creation of Decorators
# def display():
#     print('display function Ran')
# decorated_display = decorator_function(display)
# decorated_display()

# Syntax 2: using @ Symbol
@decorator_function
def display():
    print('display function Ran')

@decorator_function
def info(name,age):
    print('info function with arguments {} and {}'.format(name,age))


display()
print("\n")
info('Amrit','24')