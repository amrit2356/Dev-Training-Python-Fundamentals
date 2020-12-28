"""
Implementation of Decorators which take arguments
"""

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix,'Wrapper Executed this before: {}()'.format(original_function.__name__))
            return original_function(*args, **kwargs)
        
        return wrapper_function
    return decorator_function

@prefix_decorator('Testing: ')
def info(name,age):
    print('info function with arguments {} and {}'.format(name,age))


info('Amrit','24')