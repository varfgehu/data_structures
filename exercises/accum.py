"""
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""
def accum(s):
    sub_string_array = []
    for i in range(len(s)):
        sub_string_array.append(generate_string(i+1, s[i]))
    return '-'.join(sub_string_array)

def generate_string(count, s):
    return str(s*count).title()

print(accum("abc"))
