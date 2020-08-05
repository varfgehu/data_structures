# Given a sorted array of integers, return the two numbers such that
# they add up to a specific target. You may assume that each input
# would have exactly one solution, and you many not use the same element twice.

# Add any two element to get the target. Use only distinct elements.

A = [-2, 1, 2, 4, 7, 11]
target = 13

# Time complexity: O(n^2) ( two nested cycles)
# Space Complexity: O(1) (constant, not storing anything)
def two_sum_brute_force(A, target):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False

# A = [2, 4, 6]
# target = 10
#
# i = 0
# ht = dict()
# ht[8] = 2   # target - A[0]   10 - 2
#
# i = 1
# ht[6] = 4    # target - A[1]   10 - 4


# Time Complexity: O(n) (one cycle)
# Space Complexity: O(n) (worst case store all elements in the hash table)
def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False

# Time Complexity: O(n) (one cycle)
# Space Complexity: O(1) (not storing anything)

def two_sum(A, target):
    i = 0
    j = len(A) - 1

    while(i <= j):
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else: # A[i] + A[j] < target case
            j -= 1
    return False

print(two_sum_brute_force(A, target))
print(two_sum_hash_table(A, target))
print(two_sum(A, target))
