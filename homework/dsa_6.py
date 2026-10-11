def second_largest(nums: list) -> int:

    order = sorted(nums)
    highest = order[::-1]

    return highest[1]

nums1 = [3,7,1,9,4]
nums2 = [5,5,2]
print(second_largest(nums1))
print(second_largest(nums2))