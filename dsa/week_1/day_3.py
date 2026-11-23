# QuickCarts daily order counts are [10, 20, 30, 5, 50]. Which 3 days in a row had the most orders in total?

# def best_k_days_slow(orders: list, k):
#     if k <= 0 or k > len(orders):
#         return None

#     window_sum = 0
#     for i in range(k):
#         window_sum = window_sum + orders[i]

#     best = window_sum

#     for right in range(k, len(orders)):
#         left = right - k
#         window_sum = window_sum + orders[right] - orders[left]
#         if window_sum > best:
#             best = window_sum
#     return best

# assert best_k_days_slow([10, 20, 30, 5, 50], 3) == 85, "A failed: normal"
# assert best_k_days_slow([10, 20, 30, 5, 50], 1) == 50, "A failed: K=1 is just the max"
# assert best_k_days_slow([10, 20, 30], 3) == 60, "A failed: window = whole list"
# assert best_k_days_slow([10, 20], 3) is None, "A failed: k bigger than list"
# assert best_k_days_slow([], 1) is None, "A failed: empty"
# print("Part A passed")

# Part B
# a delivery riders rating from each trip are a list of numbers. Return the highest average over any k trips in a row,
# rounded to 2 decimals. If k is invalid, return None. [4, 2, 5, 5, 1], 2

# what is the min rating given to the rider can we give a negative rating? like -1...
# what if the rider is new joinee and has gone one ride, if averages it would be less than 1 if he got only 1 rating
# what if he gets all time the same rating like 5, 5, 5, 5....


def best_average(ratings: list, k: int):
    if k <= 0 or k > len(ratings):
        return None

    window_sum = 0
    for i in range(k):
        window_sum = window_sum + ratings[i]

    best = window_sum / k

    for right in range(k, len(ratings)):
        left = right - k

        window_sum = window_sum + (ratings[right] - ratings[left])
        window_avg = window_sum / k

        if window_avg > best:
            best = window_avg
    return round(best, 2)

assert best_average([4, 2, 5, 5, 1], 2) == 5.0, "B failed: normal"
assert best_average([3, 4, 5], 3) == 4.0, "B failed: whole list"
assert best_average([1, 2, 2], 2) == 2.0, "B failed: tie"
assert best_average([5], 2) is None, "B failed: k tool big"
print("Part B passed")