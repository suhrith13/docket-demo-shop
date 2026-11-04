"""Order helpers for a tiny demo shop."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    id: int
    customer: str
    total: float


def paginate(items, page, per_page):
    """Return one page of items. Pages are numbered from 1."""
    if page < 1 or per_page < 1:
        raise ValueError("page and per_page must be at least 1")
    start = (page - 1) * per_page
    return items[start:start + per_page]


def apply_discount(total, percent):
    """Apply a percentage discount. percent must be between 0 and 100."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(total * (1 - percent / 100), 2)


def order_history(orders, customer, page, per_page=10):
    """Return one page of a customer's orders, newest first."""
    mine = sorted(
        (o for o in orders if o.customer == customer),
        key=lambda o: o.id,
        reverse=True,
    )
    return paginate(mine, page, per_page)


def apply_loyalty_discount(total, years):
    """Loyal customers get 5% off for every year they have been with us.

    The discount is capped at 100%, so a total never goes negative.
    """
    return apply_discount(total, min(years * 5, 100))
