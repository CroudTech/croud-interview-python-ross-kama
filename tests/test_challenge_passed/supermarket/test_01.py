from src.challenges.supermarket.checkout import checkout
import pytest


def get_sku_parametrization():
    return (
        "skus,expected",
        [
            ("AAA", sum([130])),
            ("AAAA", sum([130, 50])),
            ("BB", sum([45])),
            ("AAABB", sum([130, 45])),
            ("AAABBB", sum([130, 45, 30])),
            ("AAAAAABBB", sum([200, 50, 45, 30])),
        ],
    )


@pytest.mark.parametrize(*get_sku_parametrization())
def test_checkout_01(skus, expected):
    assert checkout(skus) == expected
