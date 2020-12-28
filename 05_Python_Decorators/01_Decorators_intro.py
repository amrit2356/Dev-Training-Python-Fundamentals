"""
Implementation of Decorators in Python

"""
@
def div(a,b):        
    print(a/b)


def smart_div(func):
    def inner(a,b):
        if(a<b):
            a,b = b,a

        return func(a,b)
    
    return inner

        


div_new = smart_div(div)
div_new(4,2)