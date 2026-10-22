# Given the liset of integers, return a list of only the even numbers in order.

def even_numbers(nums: list) -> list:

    even = []

    for i in nums:
        if i % 2 ==0 :
            even.append(i)
    even.sort()
    return even

nums = [1, 2, 3, 3, 4, 4, 5, 6, 2]
print(even_numbers(nums))