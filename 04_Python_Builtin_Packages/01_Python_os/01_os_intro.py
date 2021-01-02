"""
Introduction to OS Module

"""
import os
"""
Important Functionalities:
    1. Get Current Working Directory(CWD)
    2. To Change the CWD
    3. To create a new directory.
           - To create a single sub directory
           - To create multiple sub directories(based on the path)
    4. To remove a directory.
           - To remove a single sub directory
           - To remove an entire tree of directories.
    5. List all sub directories in CWD.
"""


# To check all the possible methods and functionality available in os
print(dir(os))
# 1. To print the current working directory
print(os.getcwd())
# 3. To change the current working directory to the user provided directory.
os.chdir('/home/amrit/Documents')
print(os.getcwd())
# 4. To make a new directory
# Type 1: single directory
os.mkdir()
