"""
Write a method to replace all spaces with '%20'.
You may assume that the string has sufficient space
at the end to hol the additional characters, and
that you are given the "true" length of the string.

"""
import string

def urlify(string):
    return string.replace(" ", "%20")


print(urlify("Have you ever been to Hungary"))
