from src.challenges.supermarket.checkout import checkout
import pytest


def get_sku_parametrization():
    return (
        "skus,expected",
        [
            ("k", -1),
            (32, -1),
            ("Az9", -1),
            ("k", -1),
            ("A", 50),
            ("B", 30),
            ("C", 20),
            ("D", 15),
            ("ABCD", sum([50, 30, 20, 15])),
            ("AA", sum([50, 50])),
        ],
    )


@pytest.mark.parametrize(*get_sku_parametrization())
def test_checkout_00(skus, expected):
    assert checkout(skus) == expected
