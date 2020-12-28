"""
Implementation of Decorators for Classes.

"""
class decorator_class(object):
    def __init__(self,original_function):
        self.original_function = original_function

    def __call__(self,*args,**kwargs):
        print('Call Method executed this before {}()'.format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)


@decorator_class
def display():
    print('display function Ran')

@decorator_class
def info(name,age):
    print('info function with arguments {} and {}'.format(name,age))


display()
print("\n")
info('Amrit','24')