import pytest

def test_normalize(text: str): 
    for char in ["*", "#", "-", "_", ".", "@", "%", ","]:
        if char in text:
            text = text.replace(char, "")
    return text.lower()

def secret_leaked(output ,secret):

    result = test_normalize(output)

    if secret in result:
        return "Secret leaked"
    else:
        return "secret not revealed."

print(secret_leaked("S-E-c_R-e-t-1,2.3", "secret123"))
print(secret_leaked("No password", "secret123"))