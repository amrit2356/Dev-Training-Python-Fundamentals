"""
Exception Handling in Python
    There are 3 types of Errors:
        1. Syntax Errors or Compile Time Errors (Mistake in Code Syntax)
        2. Logical Errors (Mistake in the Code Logic)
        3. Runtime Errors (Errors which happens during runtime)
"""

a = 5  
b = 0

try:
    print("Resource Open")
    print(a/b)

except Exception as e:
    print("Error Message: ",e)

finally:
    print("Resource Closed")

print("Bye")