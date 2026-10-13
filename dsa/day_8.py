# Given a list, return a new list with duplicates removed, preserving original order.

def duplicated_removed(a: list) -> list:

    seen =[]

    for i in a:
        if i not in seen:
            seen.append(i)
    return seen

a = [3, 1, 3, 2, 1]
print(duplicated_removed(a))