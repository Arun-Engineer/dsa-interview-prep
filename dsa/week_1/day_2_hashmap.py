def count_letters(word: str) -> dict:
    counts = {}
    for letter in word:
        counts[letter] = counts.get(letter, 0) + 1
    return counts

def is_anagram(word1:str, word2:str) -> bool:
    if len(word1) != len(word2):
        return False
    return count_letters(word1) == count_letters(word2)


assert is_anagram("listen", "silent") is True, "A failed: normal"
assert is_anagram("rat", "car") is False, "A failed: different letters"
assert is_anagram("aab", "abb") is False, "A failed: same letters, different counts"
assert is_anagram("", "") is True, "A failed: both empty"
print("Part A passed")

# Part B - given a list of item names from today's order, return the item ordered most often. If two items tie, return the one that appeared 
# first in the list. If the list is empty, return None

def most_ordered(items: list):
   

   if items == []:
      return None

   counts = {}

   for item in items:
      counts[item] = counts.get(item, 0) + 1
   max_value = max(counts, key = counts.get)
   return max_value

assert most_ordered(["milk", "bread", "milk", "eggs"]) == "milk", "B failed: normal"
assert most_ordered(["bread", "milk", "milk", "bread"]) == "bread", "B failed: tie -> first"
assert most_ordered(["eggs"]) == "eggs", "B failed: one item"
assert most_ordered([]) is None, "B failed: empty"
print("Part B passed")

def most_ordered_plain(items: list):

    if not items:
        return None
    
    counts = {}

    for item in items:
        counts[item] = counts.get(item, 0) + 1

    most_ordered_item = None
    item_count = 0

    for item in items:
        if counts[item] > item_count:
            most_ordered_item = item
            item_count = counts[item]
    return most_ordered_item

assert most_ordered_plain(["milk", "bread", "milk", "eggs"]) == "milk", "plain failed: normal"
assert most_ordered_plain(["bread", "milk", "milk", "bread"]) == "bread", "plain failed: tie -> first"
assert most_ordered_plain(["eggs"]) == "eggs", "plain failed: one item"
assert most_ordered_plain([]) is None, "Plain failed: one item"
print("Plain version passed")