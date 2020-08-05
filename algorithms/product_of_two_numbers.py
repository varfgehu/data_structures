"""
Given two numbers, find theris product using recursion.
"""

x = 5
y = 7

def recursive_product(num, multiply_by):
    if multiply_by == 0:
        return 0
    else:
        return num + recursive_product(num, multiply_by - 1)

print(recursive_product(x,y))
