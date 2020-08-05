"""
Given a string, find the first uppercasse character.
Solve using both an iterative and recursive solution.
"""

input_str_1 = "gergoVarfalvi"
input_str_2 = "GergoVarfalvi"
input_str_3 = "gergovarfalvi"

def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase character found"

def find_uppercase_recursive(input_str, i=0):
    if input_str[i].isupper():
        return input_str[i]
    if i == len(input_str) - 1:
        return "No uppercase character found."
    else:
        return find_uppercase_recursive(input_str, i+1)


print("Iterative call:")
print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))

print("Recursive call:")
print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))
