"""
Given an array of integersm every element appears
twice except for one. Find that single one.

Note: Your algorithm should have
a linear runtime complexity.
Could you implement it without using extra memory?

Example:
Input: [1, 2, 2, 3, 1]
Output: 3

{ element: number of accurences }

XOR:    b1 |b2
        0   0   : 0
        0   1   : 1
        1   0   : 1
        1   1   : 0
"""
nums = [1, 2, 2, 3, 1]
ans = 0
for i in range(len(nums)):
    print("ans:" + str(ans))
    print("nums[i]:" + str(nums[i]))
    ans ^= nums[i]
    print("XOR:" + str(ans))
print("Output:" +str(ans))
