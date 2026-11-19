# A delivery system received some order IDS twice(a dupicate -order bug).
# Return the First ID tha repeats. If nothing repeats, return NOne.

# def first_repeated_order_ids(order_ids: list):
#     seen = set()

#     for order_id in order_ids:
#         if order_id in seen:
#             return order_id
#         seen.add(order_id)
#     return None

# assert first_repeated_order_ids(["A1", "B2", "C3", "B2", "A1"]) == "B2", "A failed: normal"
# assert first_repeated_order_ids(["A1", "B2"]) is None, "A failed: no repeats"
# assert first_repeated_order_ids([]) is None, "A failed: empty"
# print("Part A passed")

# A customer has a gift card for exactly budget rupees. Given a list of item prices, return the indices
# [i, j] of two different items whose prices add up to exactly budget. Return None if no such pair exits.

# what if both have the same prices exactly the budget.
# what if the pairs are within the budget lets say if budget is 100 added paris total got 99. do we need to use that pair
# what if only one item is available do and it is within the budget. do we need to add?
# Are these prices in sorted format?

# def two_sum(prices: list, budget: int):
#     prices.sort()
#     first = 0
#     last = len(prices) - 1

#     while first < last:
#         total = prices[first] + prices[last]

#         if total == budget:
#             return first, last

#         elif total < budget:
#             first = first + 1

#         else:
#             last = last - 1
#     return None

# print(two_sum([50, 20, 30, 80], 100))

# assert two_sum([50, 20, 30, 80], 100) == [1, 3], "B failed: normal (20+80)"
# assert two_sum([40, 60]) == [0, 1], "B filed: two items"
# assert two_sum([50, 50], 100) == [0,1],"B failed: duplicate prices"
# assert two_sum([50], 100) is None, "B failed: cant use same item twice"
# assert two_sum([], 100) is None, "B failed: empty"
# assert two_sum([10, 20], 100) is None, "B failed: no pair"
# print("Part B passed")

# Part B
# retry with dict {}

def two_sums(prices: list, budget: int):

    seen = {}

    for i, price in enumerate(prices):
        
        needed = budget - price

        if needed in seen:
            return [seen[needed], i]
        seen[price]= i
    return None

print(two_sums([50, 20, 30, 80], 100))
assert two_sums([50, 20, 30, 80], 100) == [1, 3], "B failed: normal (20+80)"
assert two_sums([40, 60], 100) == [0, 1], "B filed: two items"
assert two_sums([50, 50], 100) == [0,1],"B failed: duplicate prices"
assert two_sums([50], 100) is None, "B failed: cant use same item twice"
assert two_sums([], 100) is None, "B failed: empty"
assert two_sums([10, 20], 100) is None, "B failed: no pair"
print("Part B passed")