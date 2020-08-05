# You are given an array of non-negative integers. For example:
# [3, 3, 1, 0, 2, 0, 1]
# Each number represents the maximum number of steps you can advance in the array.
# Question:
# Is it possible to advance from the start of the array to the last element?
#
# Approach:
# Iterate through each entry in the array
# Track furthest we can get reach from each element ( A[i] + i)
# If any "i" before the end is the furthest, we can't reach the last index.
# Otherwise we can.


def array_advance(A):

    furthest_reached = 0
    last_index = len(A) - 1
    i = 0

    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1

    return furthest_reached >=last_index

A1 = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A1))

A2 = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A2))
