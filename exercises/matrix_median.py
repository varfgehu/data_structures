"""
Given a N cross M matrix in which each row is sorted,
find the overal median of the matrix.
Assume N*M is odd.

Example:
Matrix =
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5, so return 5.
"""

def median_matrix(A):
    if len(A) == 1:
        vec = A[0]
        return vec[len(vec)//2]
    else:
        new_list = []
        for row in range(len(A)):
            new_list.extend(A[row])
        new_list = sorted(new_list)
        print("Sorted: " + str(new_list))
    return new_list[len(new_list)//2]

l1 = [1, 3, 5]
l2 = [2, 6, 9]
l3 = [3, 6, 9]
A = [l1, l2, l3]

print(median_matrix(A))
