# 1) Add up all prices in cart. Empty cart -> 0.
def total_price(prices: list) -> float:
    total = 0
    for i in prices:
        total = total + i
    return total

# 2) Count how many times each items appears.
#  ["milk", "bread", "milk"] -> {"milk":2, "bread": 1}


def count_items(items: list) -> dict:
    counts = {}

    for item in items:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1

    return counts

def count_items1(items: list) -> dict:
    counts = {}
    for item in items:
        if item in counts:
            counts[item] = counts.get(item, 0) + 1
    return counts

# 3) Products look like JSON form an API (like Postman shows you).
# Return only the NAMES of products whose stock is more than 0.
def get_in_stock(products: list) -> list:

    # for index, inventory in enumerate(products, start = 1):
    #     if inventory["stock"] > 0:
    #         return f"{index}, {inventory["name"]} -> {inventory["stock"]} "

    inventory = []
    for stock in products:
        if stock["stock"] > 0:
            inventory.append(stock["name"])
    return inventory


# 4) Divide a by b. If b is 0, return None instead of crashing.
# You must use try/except (not an  if-check)

def safe_divide(a: float, b: float):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# 5) An Order has an id and a list of items:
# item_count() returns how many items are in the order.
class Order:

    def __init__(self, order_id: str, items: list):
        self.order_id = order_id
        self.items = items

    def item_count(self) -> int:
        return len(self.items)
    

# ---------------------- auto-checker: do not edit below -------------------------------
assert total_price([10.5, 20.0, 5.5]) == 36.0, "1 failed: normal cart"
assert total_price([]) == 0, "1 failed: empty cart"

assert count_items(["milk", "bread", "milk"]) == {"milk": 2, "bread": 1}, "2 failed"
assert count_items([]) == {}, "2 failed: empty list"

products = [
    {"name": "milk", "stock": 5},
    {"name": "eggs", "stock": 0},
    {"name": "bread", "stock": 2},
]

assert get_in_stock(products) == ["milk", "bread"], "3 failed"
assert get_in_stock([]) == [], "3 failed: empty list"

assert safe_divide(10, 2) == 5, "4 failed: normal divide"
assert safe_divide(10, 0) is None, "4 failed: divideby zero"

order = Order("ORD-101", ["milk", "eggs", "bread"])
assert order.item_count() == 3, "5 failed"
assert Order("ORD-102", []).item_count() == 0, "5 failed: empty order"

print("All 5 warm-up checks passed")