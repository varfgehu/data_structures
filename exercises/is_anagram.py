"""
Given two strings, check wheather two
given strings are anagrams of each other or not.

"""
import string
input_str_1 = "practice makes perfect"
input_str_2 = "perfect makes practice"

input_str_3 = "allergy"
input_str_4 = "allergic"

def remove_punct(string):
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for c in string:
        if c in punc:
            string.replace(c, "")
    return string

def prepare_string(string):
    string = string.replace(" ", "")
    string = string.lower()
    string = remove_punct(string)
    return string

def collect_letters(string):
    hash = dict()
    for c in string:
        if c in hash:
            hash[c] += 1
        else:
            hash[c] = 1
    return hash

def is_anagram(str_1, str_2):
    str_1 = prepare_string(str_1)
    str_2 = prepare_string(str_2)

    letters_1 = collect_letters(str_1)
    letters_2 = collect_letters(str_2)

    return letters_1 == letters_2

print(is_anagram(input_str_1, input_str_2))
print(is_anagram(input_str_3, input_str_4))
