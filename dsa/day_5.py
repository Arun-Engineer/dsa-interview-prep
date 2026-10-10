# Reverse the words in a sentence. "hello world foo" -> "foo world hello"

def reverse_words(text: str) -> str:
    """Reverse the words in a sentence."""
    word = text.split()
    return " ".join(word[::-1])

print(reverse_words("hello world foo"))