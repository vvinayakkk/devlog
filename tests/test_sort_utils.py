import sys
from pathlib import Path
import os

root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from src.sort_utils import sort_dicts

def test_sort_dicts_ascending():
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob"},
        {"name": "Charlie", "age": 25},
        {"name": "David", "age": 35},
    ]
    result = sort_dicts(data, "age")
    assert result == [
        {"name": "Charlie", "age":  25},
        {"name": "Alice", "age": 30},
        {"name": "David", "age": 35},
        {"name": "Bob"},
    ]

def test_sort_dicts_descending():
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob"},
        {"name": "Charlie", "age": 25},
        {"name": "David", "age": 35},
    ]
    result = sort_dicts(data, "age", reverse=True)
    assert result == [
        {"name": "David", "age": 35},
        {"name": "Alice", "age": 30},
        {"name": "Charlie", "age": 25},
        {"name": "Bob"},
    ]

def test_sort_dicts_missing_first():
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob"},
        {"name": "Charlie", "age": 25},
        {"name": "David", "age": 35},
    ]
    result = sort_dicts(data, "age", missing_last=False)
    assert result == [
        {"name": "Bob"},
        {"name": "Charlie", "age": 25},
        {"name": "Alice", "age": 30},
        {"name": "David", "age": 35},
    ]
