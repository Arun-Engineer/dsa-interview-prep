# Given a list of numbers, return True if any value appears more than once(has duplicates), else False

def find_duplicates(num: list) -> bool:

    seen = set()

    for i in num:
        if i in seen:
            return True
        seen.add(i)
    return False

num1 = [1, 2, 3, 1]
num2 = [1, 2, 3, 4]
print(find_duplicates(num1))
print(find_duplicates(num2))