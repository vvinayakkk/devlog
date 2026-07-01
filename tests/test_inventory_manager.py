import sys
from pathlib import Path
import pytest

# Ensure the project root directory is in the sys.path so src can be imported
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from src.inventory_manager import InventoryManager, add_to_cart, total_cart_value


def test_add_stock_adds_new_items_and_increments_existing_stock():
    """Verify that adding stock behaves correctly for new and existing items."""
    manager = InventoryManager()
    
    # Normal case: Add stock for a new item
    manager.add_stock("apple", 10)
    assert manager.stock["apple"] == 10
    
    # Normal case: Increment stock of an existing item
    manager.add_stock("apple", 5)
    assert manager.stock["apple"] == 15


def test_add_stock_raises_value_error_for_non_positive_quantity():
    """Verify that adding zero or negative stock raises a ValueError."""
    manager = InventoryManager()
    with pytest.raises(ValueError, match="Quantity to add must be greater than zero"):
        manager.add_stock("apple", 0)
        
    with pytest.raises(ValueError, match="Quantity to add must be greater than zero"):
        manager.add_stock("apple", -5)


def test_remove_stock_decreases_stock_correctly():
    """Verify that removing stock decreases stock correctly and doesn't go below zero."""
    manager = InventoryManager()
    manager.add_stock("apple", 10)
    
    manager.remove_stock("apple", 3)
    assert manager.stock["apple"] == 7
    
    # Boundary case: Remove all remaining stock
    manager.remove_stock("apple", 7)
    assert manager.stock["apple"] == 0


def test_remove_stock_raises_key_error_for_nonexistent_item():
    """Edge Case: Verify that removing stock from a nonexistent item raises a KeyError."""
    manager = InventoryManager()
    with pytest.raises(KeyError, match="Item 'banana' is not in stock"):
        manager.remove_stock("banana", 1)


def test_remove_stock_raises_value_error_for_excessive_quantity():
    """Verify that trying to remove more stock than available raises a ValueError."""
    manager = InventoryManager()
    manager.add_stock("apple", 5)
    with pytest.raises(ValueError, match="Cannot remove 6 units of 'apple'"):
        manager.remove_stock("apple", 6)


def test_remove_stock_raises_value_error_for_non_positive_quantity():
    """Verify that removing zero or negative quantity raises a ValueError."""
    manager = InventoryManager()
    manager.add_stock("apple", 10)
    
    with pytest.raises(ValueError, match="Quantity to remove must be greater than zero"):
        manager.remove_stock("apple", 0)
        
    with pytest.raises(ValueError, match="Quantity to remove must be greater than zero"):
        manager.remove_stock("apple", -3)


def test_get_low_stock_items_boundary_exactly_at_threshold():
    """Edge Case: Verify that items exactly at the low stock threshold are returned."""
    manager = InventoryManager()
    manager.add_stock("apple", 10)    # Exactly at the threshold (default 10)
    manager.add_stock("banana", 5)     # Below the threshold
    manager.add_stock("cherry", 11)    # Above the threshold
    
    low_items = manager.get_low_stock_items(threshold=10)
    assert "apple" in low_items
    assert "banana" in low_items
    assert "cherry" not in low_items


def test_get_last_n_items_when_n_equals_or_exceeds_available_items():
    """Edge Case: Verify get_last_n_items handles n >= number of items in stock without IndexError."""
    manager = InventoryManager()
    manager.add_stock("apple", 10)
    manager.add_stock("banana", 20)
    
    # Case: n equals the number of items
    assert manager.get_last_n_items(2) == ["apple", "banana"]
    
    # Case: n exceeds the number of items
    assert manager.get_last_n_items(5) == ["apple", "banana"]
    
    # Case: n is 0 or negative
    assert manager.get_last_n_items(0) == []
    assert manager.get_last_n_items(-1) == []


def test_add_to_cart_multiple_times_has_no_shared_state_leak():
    """Edge Case: Verify that successive calls to add_to_cart do not share the default cart state."""
    # First call: creates a new default cart
    cart1 = add_to_cart("apple", 2)
    assert cart1 == [("apple", 2)]
    
    # Second call: should create another new default cart (no leak from cart1)
    cart2 = add_to_cart("banana", 3)
    assert cart2 == [("banana", 3)]
    assert cart1 == [("apple", 2)]  # Make sure cart1 is unaffected


def test_total_cart_value_handles_prices_and_missing_items():
    """Verify calculating total cart value including handling items missing from price lookup."""
    cart = [("apple", 2), ("banana", 3), ("pear", 1)]
    price_lookup = {
        "apple": 1.50,
        "banana": 0.80,
        # pear is intentionally omitted
    }
    
    # total should be (2 * 1.50) + (3 * 0.80) + (1 * 0.0) = 3.00 + 2.40 + 0.0 = 5.40
    assert total_cart_value(cart, price_lookup) == 5.40
