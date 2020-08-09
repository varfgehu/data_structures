"""
Given an integer as input.
Convert the integer you are given to a string.
Do not make use of the built-in "str" function.

str(123) --> '123'
"""

def int_to_str(input_int):
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []

    while input_int > 0:
        output_str.append(chr(ord('0') + input_int % 10))
        # print(input_int % 10)
        input_int //= 10
    output_str = output_str[::-1]
    # print(output_str)

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str

print(int_to_str(-123))
