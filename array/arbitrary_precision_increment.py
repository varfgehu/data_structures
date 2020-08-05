# Given:
# An array of non-negative digits that represents a decimal integer.
# For example: A = [1, 4, 9]
#
# Problem:
# Add one to the represented integer.
# Solution for the example above [1, 5, 0]
#
# Solution:
# Add 1 to the rightmost digit
# Propagate carry throughout the array.
# (Similar to the standard primary school approach)
# If there is a carry at the leftmost digit, add that digit to the beginning od the array.

A1 = [1,4,9]
A2 = [9, 9, 9]
# string = ''.join(map(str,A))
# print(string)
# print(int(string) + 1)

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

print(plus_one(A1))
print(plus_one(A2))
