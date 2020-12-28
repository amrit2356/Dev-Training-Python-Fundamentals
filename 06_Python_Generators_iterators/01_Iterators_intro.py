"""
Implementation of Iterators in Python
"""


nums = [7,6,9,2]

# it =iter(nums)
# print(it.__next__())
# print(it.__next__())
# print(next(it))


#### Implementation of User Defined Iterator
class TopTen:
    def __init__(self):
        self.num =1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num +=1
        return val

values = TopTen()

for i in range(0,10):
    print(values.__next__())