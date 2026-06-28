"""Basic calculator operations for division, averaging, and finding maximum values.

This module provides small numeric utilities for common sequence operations.
Each function validates its inputs and raises ValueError for invalid cases.
"""

from collections.abc import Sequence
from typing import TypeVar

Number = float | int
T = TypeVar("T")


def divide(a: Number, b: Number) -> float:
    """Return ``a`` divided by ``b``.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient of ``a`` and ``b``.

    Raises:
        ValueError: If ``b`` is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def get_average(nums: Sequence[Number]) -> float:
    """Return the arithmetic mean of ``nums``.

    Args:
        nums: A non-empty sequence of numbers.

    Returns:
        The average of the values in ``nums``.

    Raises:
        ValueError: If ``nums`` is empty.
    """
    if not nums:
        raise ValueError("Cannot compute average of an empty sequence")
    return sum(nums) / len(nums)


def find_max(items: Sequence[T]) -> T:
    """Return the largest value in ``items``.

    Args:
        items: A non-empty sequence of comparable values.

    Returns:
        The maximum element in ``items``.

    Raises:
        ValueError: If ``items`` is empty.
    """
    if not items:
        raise ValueError("Cannot find max of an empty sequence")
    max_val = items[0]
    for item in items:
        if item > max_val:
            max_val = item
    return max_val


if __name__ == "__main__":
    for label, fn in [
        ("divide(10, 0)", lambda: divide(10, 0)),
        ("get_average([])", lambda: get_average([])),
        ("find_max([])", lambda: find_max([])),
    ]:
        try:
            print(f"{label} = {fn()}")
        except ValueError as e:
            print(f"{label} failed: {e}")
