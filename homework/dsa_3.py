# First_duplicate(nums) - return the first value that appears twice, or NONE.

def first_duplicate(nums):
    seen = set()

    first = nums[0]

    for i in nums:
        if i == first:
            if i in seen:
                return True
            seen.add(i)
    return None

nums1 = [1, 2, 3, 15, 1]
nums2 = [1, 2, 3, 4, 5]
print(first_duplicate(nums1))
print(first_duplicate(nums2))