# First_duplicate(nums) - return the first value that appears twice, or NONE.

def first_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None

nums1 = [1, 2, 3, 15, 1]
nums2 = [1, 2, 3, 4, 5]
nums3 = [2, 1, 3, 3, 4]
print(first_duplicate(nums1))
print(first_duplicate(nums2))
print(first_duplicate(nums3))