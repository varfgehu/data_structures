def binary_array_to_number(input_array):
    array = []
    for c in input_array:
        array.append(str(c))
    input_string = ''.join(array)
    res = int("0b" + input_string, 2)
    return res



array = [0,0,0,1]

print(binary_array_to_number(array))
