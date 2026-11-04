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
