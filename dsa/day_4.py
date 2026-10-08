def find_anagrams(text1: str, text2: str) -> bool:
    a = {}
    b = {}

    for i in text1:
        a[i] = a.get(i, 0) + 1
    for j in text2:
        b[j] = b.get(j, 0) + 1
    if a != b:
        return False
    return True

texts1 = "listen"
texts2 = "silent"
print(find_anagrams(texts1, texts2))
print(find_anagrams("hello", "world"))