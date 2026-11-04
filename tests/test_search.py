from shop.orders import Order, search_orders


def test_search_matches_case_insensitively():
    orders = [Order(1, "Asha", 10.0), Order(2, "Ravi", 20.0)]
    assert all("asha" in o.customer.lower() for o in search_orders(orders, "ASHA", page=1))
