from dsa.dsa_10_1 import *

def test_pair_sum():
    prices = [10, 20, 35, 50, 75, 80]
    assert pair_sum(prices, 70) == (20, 50)
    assert pair_sum(prices, 1000) is None
    assert pair_sum([], 5) is None
    assert pair_sum([5], 10) is None
    assert pair_sum([5, 5], 10) == (5, 5)

def test_both_versions_agree():
    prices = [10, 20, 35, 50, 75, 80]
    for target in [30, 70, 85, 155, 999]:
        assert pair_sum(prices, target) == pair_sum_brute(prices, target)