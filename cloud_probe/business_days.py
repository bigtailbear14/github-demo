"""Business-day arithmetic with Monday through Friday as business days."""

from datetime import date, timedelta


def add_business_days(start: date, days: int) -> date:
    """Add business days after start, excluding weekends (no holiday calendar).

    Zero returns start unchanged, including when start falls on a weekend.
    Negative days raise ValueError.
    """
    if days < 0:
        raise ValueError("days must be non-negative")
    result = start
    while days:
        result += timedelta(days=1)
        if result.weekday() < 5:
            days -= 1
    return result
