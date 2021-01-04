"""
How to use os.walk() function
"""
import os
path = '/home/amrit/Documents'
for dirpath, dirnames, filenames in os.walk(path):
    print('Current Path: {}'.format(dirpath))
    print('Directories {}'.format(dirnames))
    print('filenames: {}'.format(filenames))
