"""
Given some integer, n.
Determine the n-th term in the "look_and_say" sequence.
 n = 4, sequence: 1211

1
11
21
1211
111221
312211
13112221
"""


def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i +1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

s = "1"
n = 4
for i in range(n-1):
    s = next_number(s)
    print(s)
