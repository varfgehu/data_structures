# Given an arrany of integers, return INDICES (plural of index) of
# the two numbers such that they add up to a
# specific target.

# You may assume that each inout would have
# exactly one solution, and you may not use the
# same element twice.

# Example:
# nums = [1, 3, 11, 2, 7]
# target = 9
# return [3,4]

nums = [1, 3, 11, 2, 7]
target = 9

def two_sum(nums, target):
    if len(nums) <= 1:
        return False

    aux_dict = dict()
    for i in range(len(nums)):
        if nums[i] in aux_dict:
            return [aux_dict[nums[i]], i]
        else:
            aux_dict[target-nums[i]] = i

print(two_sum(nums, target))
