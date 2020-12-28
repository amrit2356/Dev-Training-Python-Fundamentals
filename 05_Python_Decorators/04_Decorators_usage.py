"""
Usage of Decorators in Projects
  -logging
  -Timing of functionality
"""
import os
import time
import logging
from functools import wraps
def my_logger(original_func):
    os.chdir('05_Python_Decorators/logs')
    logging.basicConfig(filename='{}.log'.format(original_func.__name__),level=logging.INFO)
    @wraps(original_func)
    def wrapper(*args,**kwargs):
        logging.info('Ran with args {}, and kwargs {}'.format(args,kwargs))
        return original_func(*args, **kwargs)
    return wrapper

def my_timer(original_func):
    @wraps(original_func)
    def wrapper(*args,**kwargs):
        start_time =time.time()
        time.sleep(1)
        result = original_func(*args,**kwargs)
        end_time =time.time()
        print('{}() ran in: {}secs'.format(original_func.__name__,(end_time-start_time)))
        return result
    return wrapper


@my_logger
@my_timer
def display_info(name,age):
    print('Diplay_info ran with arguments({},{})'.format(name,age))


display_info('Hank',30)
