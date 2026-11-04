import pytest

from shop.orders import apply_discount, paginate


def test_first_page_starts_at_first_item():
    assert paginate(list(range(25)), page=1, per_page=10) == list(range(10))


def test_last_page_is_partial():
    assert paginate(list(range(25)), page=3, per_page=10) == list(range(20, 25))


def test_page_zero_is_rejected():
    with pytest.raises(ValueError):
        paginate([1, 2, 3], page=0, per_page=10)


def test_discount():
    assert apply_discount(200.0, 25) == 150.0


def test_discount_over_100_is_rejected():
    with pytest.raises(ValueError):
        apply_discount(100.0, 150)
