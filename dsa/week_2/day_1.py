def merge_sorted(a, b):
    # Step 1: One finger at the start of each list, plus an empty result

    i = 0
    j = 0
    result = []

    # Step 2: While BOTH lists still have people left
    while i < len(a) and j < len(b):
        # Step 3: The smaller front item goes next, and that finger moves
        if a[i] <= b[j]:
            result.append(a[i])
            i = i + 1
        else:
            result.append(b[j])
            j = j + 1

    # Step 4: One list is finished, so add whatever is left in the other
    while i < len(a):
        result.append(a[i])
        i = i + 1
    while j < len(b):
        result.append(b[j])
        j = j + 1

    return result

assert merge_sorted([1, 4, 7], [2, 3, 9]) == [1, 2, 3, 4, 7, 9], "normal"
assert merge_sorted([], [1, 2]) == [1, 2], "first list empty"
assert merge_sorted([1, 2], []) == [1, 2], "second list empty"
assert merge_sorted([], []) == [], "both empty"
assert merge_sorted([2, 2], [2]) == [2, 2, 2], "duplicates kept"
print("Part A: all tests passed")

# Part B: Given a sorted list of prices and a budget, return the two prices(not positions)
# that addup exactly to the budget. Return an empty list if there's no pair.

#questions- does two lists have same length?
# what if the single value matches in the one list itself?
# what if two parirs satisfy our budget which to choose?

def sorted_pairs(a: list, b: list, budget: int):

    first_list = 0
    second_list = len(b) - 1

    while first_list < len(a) and second_list >= 0:

        sum = a[first_list] + b[second_list]

        if sum == budget:
            return [a[first_list], b[second_list]]

        elif sum > budget:
            second_list = second_list - 1

        else:
            first_list = first_list + 1

    return[]

assert sorted_pairs([100, 150, 200], [50, 100, 350], 300) == [200, 100]
assert sorted_pairs([], [150, 300], 300) == []
assert sorted_pairs([],[], 300) == []
assert sorted_pairs([100, 150, 200], [400, 450, 500], 300) == []
assert sorted_pairs([100, 150, 200], [50, 100], 300) == [200, 100]
assert sorted_pairs([100, 150, 200], [150, 200, 250], 300) == [100, 200]
print("Part B: All tests passed")