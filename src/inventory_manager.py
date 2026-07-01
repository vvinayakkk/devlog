"""Inventory management module for devlog — tracks stock and cart operations."""

from typing import Dict, List, Tuple, Optional


class InventoryManager:
    """Manages product stock levels and inventory operations."""

    def __init__(self) -> None:
        """Initialize the InventoryManager with empty stock."""
        self.stock: Dict[str, int] = {}

    def add_stock(self, item_name: str, quantity: int) -> None:
        """Add stock for an item.

        Args:
            item_name: The name of the item.
            quantity: The quantity to add. Must be positive.

        Raises:
            ValueError: If quantity is less than or equal to 0.
        """
        if quantity <= 0:
            raise ValueError("Quantity to add must be greater than zero.")
        self.stock[item_name] = self.stock.get(item_name, 0) + quantity

    def remove_stock(self, item_name: str, quantity: int) -> None:
        """Remove stock for an item.

        Args:
            item_name: The name of the item.
            quantity: The quantity to remove. Must be positive and less than or equal to available stock.

        Raises:
            KeyError: If the item does not exist in stock.
            ValueError: If quantity is less than or equal to 0 or exceeds available stock.
        """
        if item_name not in self.stock:
            raise KeyError(f"Item '{item_name}' is not in stock.")
        if quantity <= 0:
            raise ValueError("Quantity to remove must be greater than zero.")
        if self.stock[item_name] < quantity:
            raise ValueError(
                f"Cannot remove {quantity} units of '{item_name}'. Only {self.stock[item_name]} units available."
            )
        
        self.stock[item_name] -= quantity

    def get_low_stock_items(self, threshold: int = 10) -> List[str]:
        """Return items whose stock is at or below the threshold.

        Args:
            threshold: The stock level threshold (inclusive). Defaults to 10.

        Returns:
            A list of item names that are low in stock.
        """
        low_items = []
        for item, qty in self.stock.items():
            if qty <= threshold:
                low_items.append(item)
        return low_items

    def get_last_n_items(self, n: int) -> List[str]:
        """Return the last n items added to stock, in insertion order.

        Args:
            n: The number of items to retrieve.

        Returns:
            A list of the last n items.
        """
        if n <= 0:
            return []
        items = list(self.stock.keys())
        return items[-n:]


def add_to_cart(
    item_name: str, quantity: int, cart: Optional[List[Tuple[str, int]]] = None
) -> List[Tuple[str, int]]:
    """Add an item to the shopping cart and return the cart.

    Args:
        item_name: The name of the item.
        quantity: The quantity of the item.
        cart: An optional existing cart. If None, a new cart is created.

    Returns:
        The updated shopping cart.
    """
    if cart is None:
        cart = []
    cart.append((item_name, quantity))
    return cart


def total_cart_value(cart: List[Tuple[str, int]], price_lookup: Dict[str, float]) -> float:
    """Calculate total value of items in the cart.

    Args:
        cart: The shopping cart containing (item_name, quantity) tuples.
        price_lookup: A dictionary mapping item names to their prices.

    Returns:
        The total value of the items in the cart.
    """
    total = 0.0
    for item_name, quantity in cart:
        total += price_lookup.get(item_name, 0.0) * quantity
    return total