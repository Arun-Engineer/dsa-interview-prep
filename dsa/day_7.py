# Given two sorted lists, merge them into one sorted list.

def merge_sorted_list(list1: list, list2: list) -> list:
    """Given two sorted lists merge them into one sorted list."""
    merge_list = list1 + list2

    sorted_list = sorted(merge_list)

    return sorted_list

list1 = [1,3,5]
list2 = [2,4,6]
print(merge_sorted_list(list1,list2)) 