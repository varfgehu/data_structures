# Given two stringsm write a function to decide
# if one is a permutation of the other

# "driving"
# "drivign"   <-- Permutation

# "driving"
# "ddriving"   <-- Not a Permutation

def collect(string, hash):
    for c in string:
        if c in hash:
            hash[c] += 1
        else:
            hash[c] = 1
    return hash

def is_permutation(string1, string2):
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    if len(string1) != len(string2):
        return False

    letters1 = dict()
    letters2 = dict()

    letters1 = collect(string1, letters1)
    letters2 = collect(string2, letters2)

    print(letters1)
    print(letters2)

    return letters1 == letters2


print(is_permutation("drived", "devird"))
