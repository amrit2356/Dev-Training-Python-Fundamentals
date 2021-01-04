"""
Introduction to OS Module
"""
import os
"""
Important Functionalities:
    1. Get Current Working Directory(CWD)
    2. To Change the CWD
    3. List all sub directories in CWD.
    4. To create a new directory.
           - To create a single sub directory
           - To create multiple sub directories(based on the path)
    5. To remove a directory.
           - To remove a single sub directory
           - To remove an entire tree of directories.
    6. Renaming a Directory
    7. Get the Stats data for the File.
"""


# To check all the possible methods and functionality available in os
print(dir(os))

# 1. To print the current working directory
print(os.getcwd())

# 2. To change the current working directory to the user provided directory.
os.chdir('/home/amrit/Documents')
print(os.getcwd())

# 3. To list all subdirectories, in the path mentioned
print(os.listdir(os.getcwd()))

# 4. To make a new directory
# Type 1: single directory
os.mkdir('/home/amrit/Documents/test')

# Type 2: To create multiple sub directories(based on the path)
os.makedirs('/home/amrit/Documents/multiple_directories/test_multi_direct')

# 5. To remove directories:
# Type 1: single directory
os.rmdir('/home/amrit/Documents/test')

# Type 2: To create multiple sub directories(based on the path)
os.chdir('/home/amrit/Documents')
os.removedirs('multiple_directories/test_multi_direct')

# 6. Renaming a directory
root = '/home/amrit/Documents//Dev Training-Python Fundamentals'
path = '{}/03_Python_File_Handling'.format(root)
os.chdir(path)
os.rename('text.txt', 'new_name_test.txt')

# 7. Viewing Stats of a file.
print(os.stat('new_name_test.txt'))
