# Frequency count pattern again new problem
# most_frequent_char(word) - return the character that appears most times.(same counting pattern as today, different question)

def most_frequent_chat(word):
    counts ={}

    for char in word:
        counts[char] = counts.get(char, 0) + 1

    max_char = ""
    highest_count = 0
    for char, count in counts.items():
        if count > highest_count:
            highest_count = count
            max_char = char
    return f"This letter -> {max_char} in this word -> {word}, repeated {highest_count} times."

print(most_frequent_chat("aeroplane"))