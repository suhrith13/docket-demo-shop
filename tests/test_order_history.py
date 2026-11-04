from shop.orders import Order, apply_loyalty_discount, order_history


def make_orders():
    return [Order(id=i, customer="asha" if i % 2 else "ravi", total=10.0 * i) for i in range(1, 41)]


def test_history_only_has_the_customers_orders():
    page = order_history(make_orders(), "asha", page=1)
    assert all(o.customer == "asha" for o in page)


def test_loyalty_discount_two_years():
    assert apply_loyalty_discount(100.0, 2) == 90.0
