from shop.orders import Order, average_order_total


def test_average_of_orders():
    orders = [Order(1, "Asha", 10.0), Order(2, "Ravi", 20.0), Order(3, "Asha", 45.0)]
    assert average_order_total(orders) == 25.0


def test_average_with_no_orders_is_zero():
    assert average_order_total([]) == 0.0
