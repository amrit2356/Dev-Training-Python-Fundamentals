"""
OS.path module
    This module is responsible for the manipulation of paths
used to parse the folder directories in the memory.
"""
import os.path

# Get Environment Variables
print(os.getenv('HOME'))

# Creation of file path(without using '/')
file_path = os.path.join(os.environ.get('HOME'), 'text.txt')
print(file_path)


# Getting the basename of the path
print('Path Provided: {}'.format('/tmp/text.txt'))
print('BaseName of the Path: {}'.format(os.path.basename('/tmp/text.txt')))

# Getting the directory name of the path
print('Directory of the Path: {}'.format(os.path.dirname('/tmp/text.txt')))

# To check whether path exists
print(os.path.exists('tmp/text.txt'))
