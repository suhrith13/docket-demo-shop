import pytest

from shop.orders import Order, search_orders


def test_search_matches_case_insensitively():
    orders = [Order(1, "Asha", 10.0), Order(2, "Ravi", 20.0)]
    assert [o.id for o in search_orders(orders, "ASHA", page=1)] == [1]


def test_search_page_one_is_first_results():
    orders = [Order(i, "Asha", 10.0) for i in range(1, 26)]
    assert [o.id for o in search_orders(orders, "asha", page=1)] == list(range(1, 11))
    assert [o.id for o in search_orders(orders, "asha", page=3)] == list(range(21, 26))


def test_search_page_zero_is_rejected():
    with pytest.raises(ValueError):
        search_orders([Order(1, "Asha", 10.0)], "asha", page=0)


def test_search_with_no_match_is_empty():
    assert search_orders([Order(1, "Asha", 10.0)], "zed", page=1) == []
