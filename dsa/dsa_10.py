def rotate_left(s, k):

    if s == "" or k == 0:
        return s

    if len(s) == k :
        return s
    
    if len(s) > k:
        for i in range(k+1):
            rotated = s[i:] + s[:i]
        return rotated

    if len(s) < k:
        k = k - len(s)
        for i in range(k+1):
            rotate = s[i:] + s[:i]
        return rotate

print(rotate_left("abcdef", 2))
print(rotate_left("abcdef", 6))
print(rotate_left("abcdef", 10))
print(rotate_left("abcdef", 3))