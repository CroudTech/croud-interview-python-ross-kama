from typing import NamedTuple, Optional
from collections import Counter


class Offer(NamedTuple):
    count: int
    price: int
    free_item: Optional[str] = None


def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    offers = {
        "A": [Offer(count=5, price=200), Offer(count=3, price=130)],
        "B": [Offer(count=2, price=45)],
        "E": [Offer(count=2, price=80, free_item="B")],
    }
    total = 0

    # Calculate the total price
    sku_counts = Counter(skus)
    for sku, count in sku_counts.items():
        if sku.upper() in prices:
            if sku in offers:
                for offer in offers[sku]:
                    while count >= offer.count:
                        total += offer.price
                        count -= offer.count
                        if offer.free_item and sku_counts[offer.free_item] > 0:
                            sku_counts[offer.free_item] -= 1
            total += prices[sku] * count
        else:
            return -1

    return total
