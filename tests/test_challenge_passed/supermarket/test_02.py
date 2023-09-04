from src.challenges.supermarket.checkout import checkout
import pytest


def get_sku_parametrization():
    return (
        "skus,expected",
        [
            ("A" * 5, sum([200])),
            ("A" * 8, sum([130, 200])),
            ("E", sum([40])),
            ("EEB", sum([40, 40])),
            ("EEBEEB", sum([40, 40, 40, 40])),
            ("EEBEEBB", sum([40, 40, 40, 40, 30])),
        ],
    )


@pytest.mark.parametrize(*get_sku_parametrization())
def test_checkout_02(skus, expected):
    assert checkout(skus) == expected
