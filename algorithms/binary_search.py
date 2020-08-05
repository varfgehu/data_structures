data = [2,4,5,7,8,9,12,14,17,22,25,27,28,33,37]
target = 28


# Linear search
def linear_search(data, target):
    steps = 0
    for i in range(len(data)):
        steps += 1
        if data[i] == target:
            print("Item found in " + str(steps) + " steps")
            return True
    return False


def binary_search(data, target):
    low = 0
    high = len(data) -1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if target == data[mid]:
            print("Item found in " + str(steps) + " steps")
            return True
        elif target < data[mid]:
            high = mid -1
        else:
            low = mid + 1
    return False

# Recursive binray search
def recursive_binary(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (high + low) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return recursive_binary(data, target, low, mid-1)
        else:
            return recursive_binary(data, target, mid+1, high)


print(linear_search(data, target))
print(binary_search(data, target))
print(recursive_binary(data, target, 0, len(data)))
