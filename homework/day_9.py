# string rotation

# def rotation(text1: str, text2: str) -> bool:

#     if len(text1)!= len(text2):
#         return False

#     return text2 in (text1+text1)

# print(rotation("abcde", "cdeab"))
# print(rotation("abcde", "abced"))
# print(rotation("abcde", "xyz"))
# print(rotation("hello", "llohe"))
# print(rotation("", ""))

# rotate_left(s,k)

def rotate_left(s , k):

    if k == 0:
        return s
    elif len(s) < k:
        quotient = k % len(s)
        for i in range(quotient):
            rotate = s[(i+1):] + s[:(i+1)]
        return rotate
    else:
        for i in range(k):
            rotated = s[(i+1):] + s[:(i+1)]
        return rotated

print(rotate_left("abcde", 1))
print(rotate_left("abcde", 2))
print(rotate_left("abcde", 0))
print(rotate_left("abcde", 5))
print(rotate_left("abcde", 7))

def rotations(s1, s2):

    if s1 == "":
        return False
    elif len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            rotated = s1[i:] + s1[:i]

            if rotated == s2:
                return True
        return False

print(rotations("abcde", "cdeab"))
print(rotations("abcde", "abced"))
print(rotations("abcde", "xyz"))
print(rotations("hello", "llohe"))
print(rotations("", ""))

def rotation_index(s1, s2):

    if len(s1) != len(s2):
        return -1

    for i in range(len(s1)):
        rotated = s1[i:] + s1[:i]

        if rotated == s2:
            return i
    return -1

print(rotation_index("abcde", "cdeab"))
print(rotation_index("abcde", "abced"))
print(rotation_index("abcde", "xyz"))
print(rotation_index("hello", "llohe"))