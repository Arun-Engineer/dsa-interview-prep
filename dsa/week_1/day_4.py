# Part A - Worked example (new concept, so type it yourself, dont paste)

def pair_with_sum(prices: list, target: int) -> dict:

    left = 0
    right = len(prices) - 1

    while left < right:
        sum = prices[left] + prices[right]

        if sum == target:
            return [left, right]

        elif sum > target:
            right = right - 1

        else:
            left = left + 1

    return []


print(pair_with_sum([100, 150, 200, 350, 450], 500))

assert pair_with_sum([100, 150, 200, 350, 450], 500) == [1, 3], "150 + 350"
assert pair_with_sum([100, 150, 200], 1000) == [], "no pair adds up"
assert pair_with_sum([], 500) == [], "empty list"
assert pair_with_sum([250], 500) == [], "one item cant pair with itself"
assert pair_with_sum([250, 250], 500) == [0, 1], "two equal items"
print("Part A: all tests passed")

# Part B - Write is_palindrome(word). It should return True if the word reads the same forwards and
# backwards, like 'level' or 'racecar'. Dont build a reversal copy of the string.


# what if empty "" is given as input.
# what if empty "" is given as input


def is_palindrome(word):

    if len(word) != len(word[::-1]):
        return False

    reverse = word[::-1]

    return word.lower() == reverse.lower()

assert is_palindrome("Level") == True
assert is_palindrome("racecar") == True
assert is_palindrome("cat") == False
assert is_palindrome("carracer") == False
print("Part B: All test passed.")


def is_palindrome(word):

    left = 0
    right = len(word) - 1

    while left < right:

        if word[left].lower() != word[right].lower():
            return False
        left = left + 1
        right = right - 1
    return True

assert is_palindrome("Level") == True
assert is_palindrome("racecar") == True
assert is_palindrome("cat") == False
assert is_palindrome("carracer") == False
print("Part B: All test passed.")