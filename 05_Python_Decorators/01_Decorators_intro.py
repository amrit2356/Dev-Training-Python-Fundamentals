"""
Implementation of Decorators in Python

"""
def decorator_function(original_function):
    def wrapper_function():
        print('Wrapper Executed this before: {}()'.format(original_function.__name__))
        return original_function()
    
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

display()
