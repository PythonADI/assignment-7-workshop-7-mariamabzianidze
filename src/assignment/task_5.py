"""
Create a function called calculate_sum that accepts any number of numbers as arguments (using *args). The function should return the sum of all numbers passed in.

Call calculate_sum with varying numbers of arguments (e.g., calculate_sum(1, 2, 3) and calculate_sum(5, 10, 15, 20)).
"""

def calculate_sum(*args):
    
    return sum(args)


print(calculate_sum(1, 2, 3, 4))
print(calculate_sum(5, 6, 7))
print(calculate_sum(8, 9))
print(calculate_sum())


print(calculate_sum(1, 2, 3))
print(calculate_sum(5, 10, 15, 20))    
