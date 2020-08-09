"""
ou are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption
"""
def longest_consec(strarr, k):
    print("k = " + str(k))
    print("strarr = " + str(strarr))

    n = len(strarr)
    print("n = " + str(n))
    if n == 0 or k > n or k <= 0:
        return ""

    top_len = 0
    return_string = ""
    for i in range(n+1):
        print("i = " + str(i))
        test_string = ""
        for j in range(k):
            print("j = " + str(j))
            if i+j > n - 1:
                break
            test_string += strarr[j+i]
            print("test_string = " + test_string)
        if len(test_string) > top_len:
            top_len = len(test_string)
            return_string = test_string
            print("top_len = " + str(top_len))
            print("return_string = " + return_string)
    return return_string


print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))
