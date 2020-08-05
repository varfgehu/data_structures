"""
Given a string, count the number of constants.
Note a constant is a letter that is not a vowel.
a letter that is not a, e, i, o, or u.
"""

input_str_1 = "abc de"
input_str_2 = "GerGoVarFalvI"

def prepare_string(str):
    str = str.lower()
    str = str.replace(" ", "")
    return str


def count_constants(input_str):
    input_str = prepare_string(input_str)
    constants = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in range(len(input_str)-1):
        if input_str[i] not in constants:
            count += 1
    return count

def recursive_count_constants(input_str):
    constants = ['a', 'e', 'i', 'o', 'u']
    input_str = prepare_string(input_str)
    if input_str == "":
        return 0
    else:
        if input_str[0:1] not in constants:
            # print(input_str[0:1])
            return 1 + recursive_count_constants(input_str[1:])
        else:
            return recursive_count_constants(input_str[1:])

print(count_constants(input_str_1))
print(count_constants(input_str_2))

print("\n Recursive:")
print(recursive_count_constants(input_str_1))
print(recursive_count_constants(input_str_2))
