"""
Python Comprehension 
    - Single line syntax to populate lists, tuples,sets or dictionaries
"""
nums = [1,2,3,4,5,6,7,8,9,10]

my_list = []

#Standard method of creation of list using for loop
for n in nums:
    my_list.append(n)
print("Standard For loop Code: ",my_list)

# Implementation of List Comprehension
my_list_comprehension = [n for n in nums]
print("List Comprehension: ",my_list_comprehension)

# n*n list Comprehension
n_sq_list =[n*n for n in nums]
print("n*n List: ",n_sq_list)

# list should have even nos only(with a condition)
n_even_list = [n for n in nums if(n%2==0)]
print("List of Even No: ",n_even_list)


my_list = []
## Multiple for loop list Comprehensions
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))

print(my_list)

## List Comprehension implementation for multiple for loops
my_list = []
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]

print(my_list)