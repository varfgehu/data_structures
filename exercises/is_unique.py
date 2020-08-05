# Implement an algorithm to determine
# if a string has all unique characters.

# "unique" --> False
# "auto" --> True

def is_unique(string):
    letters = dict()
    for i in string:
        if i in letters:
            return False
        else:
            letters[i] = 1
    return True

print(is_unique("unique"))
print(is_unique("auto"))
