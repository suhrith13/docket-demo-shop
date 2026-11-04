import pytest

from shop.orders import Order, apply_loyalty_discount, order_history


def make_orders():
    return [Order(id=i, customer="asha" if i % 2 else "ravi", total=10.0 * i) for i in range(1, 41)]


def test_history_only_has_the_customers_orders():
    page = order_history(make_orders(), "asha", page=1)
    assert all(o.customer == "asha" for o in page)


def test_history_page_one_is_newest_orders():
    orders = [Order(id=i, customer="asha", total=10.0) for i in range(1, 26)]
    assert [o.id for o in order_history(orders, "asha", page=1)] == list(range(25, 15, -1))
    assert [o.id for o in order_history(orders, "asha", page=3)] == [5, 4, 3, 2, 1]


def test_history_page_zero_is_rejected():
    with pytest.raises(ValueError):
        order_history(make_orders(), "asha", page=0)


def test_loyalty_discount_two_years():
    assert apply_loyalty_discount(100.0, 2) == 90.0


def test_loyalty_discount_is_capped_at_100_percent():
    assert apply_loyalty_discount(100.0, 20) == 0.0
    assert apply_loyalty_discount(100.0, 25) == 0.0


def test_loyalty_discount_negative_years_rejected():
    with pytest.raises(ValueError):
        apply_loyalty_discount(100.0, -1)
