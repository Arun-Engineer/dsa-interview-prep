# given a string return the character that appears most frequently

def frequent_characters(texts: str) -> str:

    char = {}

    for text in texts:
        char[text] = char.get(text, 0) + 1

    return max(char, key = char.get)

print(frequent_characters("aabbbc"))
print(frequent_characters("hello"))