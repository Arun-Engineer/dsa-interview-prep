# check given string is palindrome or not

def palindrome(text: str) -> str:
    rev = text[::-1]
    a = []
    b = []

    for i in text:
        a.append(i)
    for j in rev:
        b.append(j)
    if a == b:
        return True
    else:
        return False

text1= "racecar"
text2= "hello"
print(palindrome(text1))
print(palindrome(text2))

def check_palindrome(text: str) -> bool:
    return text == text[::-1]

text1= "racecar"
text2= "hello"
print(check_palindrome(text1))
print(check_palindrome(text2))