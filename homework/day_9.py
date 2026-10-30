# string rotation

def rotation(text1: str, text2: str) -> bool:

    if len(text1)!= len(text2):
        return False

    return text2 in (text1+text2)

print(rotation("abcde", "cdeab"))
print(rotation("abcde", "abced"))
print(rotation("abcde", "xyz"))
print(rotation("hello", "llohe"))
print(rotation("", ""))