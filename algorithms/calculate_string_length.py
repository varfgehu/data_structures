"""
Given a strig, calculate the length of the string
"""

input_str = "GergoVarfalvi"

print(len(input_str))

def iterative_string_length(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count

def recursive_string_length(input_str):
    if input_str == "":
        return 0
    else:
        return 1 + recursive_string_length(input_str[1:])


print(iterative_string_length(input_str))
print(recursive_string_length(input_str))
