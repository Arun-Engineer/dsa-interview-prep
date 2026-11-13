# simple version
def pair_sum_brute(nums, target):
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (nums[i],nums[j])
    return None

# Two pointer version
def pair_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return (nums[left], nums[right])
        elif total < target:
            left = left + 1
        else:
            right = right - 1
    return None



if __name__ == "__main__":
    prices = [10, 20, 35, 50, 75, 100]
    print(pair_sum_brute(prices, 70))
    print(pair_sum(prices, 70))