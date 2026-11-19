def two_sum(prices: list, budget: int):

    seen = {}

    for i, price in enumerate(prices):
        need = budget - price

        if need in seen:
            return [seen[need], i]
        seen[price] = i
    return None

assert two_sum([50, 20, 30, 80], 100) == [1, 3], "normal"
assert two_sum([40, 60], 100) == [0, 1], "two itmes"
assert two_sum([50, 50], 100) == [0, 1], "duplicate prices"
assert two_sum([50], 100) is None, "same item twice"
assert two_sum([], 100) is None, "empty"
assert two_sum([10, 20], 100) is None, "no pair"
print("W1 passed")