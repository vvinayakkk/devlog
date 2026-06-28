"""Tests for buggy_calculator: divide, get_average, and find_max."""

import subprocess
import sys
from pathlib import Path

import pytest

from buggy_calculator import divide, find_max, get_average

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = PROJECT_ROOT / "src" / "buggy_calculator.py"


class TestDivide:
    """Tests for divide(a, b)."""

    @pytest.mark.parametrize(
        ("a", "b", "expected"),
        [
            (10, 2, 5.0),
            (7, 2, 3.5),
            (-10, 2, -5.0),
            (10, -2, -5.0),
            (-10, -2, 5.0),
            (0, 5, 0.0),
            (1, 3, 1 / 3),
            (2.5, 0.5, 5.0),
        ],
        ids=[
            "integers",
            "non-integer-result",
            "negative-numerator",
            "negative-denominator",
            "both-negative",
            "zero-numerator",
            "repeating-decimal",
            "float-operands",
        ],
    )
    def test_normal_cases(self, a, b, expected):
        assert divide(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize("divisor", [0, 0.0, -0.0])
    def test_divide_by_zero_raises(self, divisor):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, divisor)

    def test_zero_numerator_with_float_divisor(self):
        assert divide(0, 2.5) == 0.0


class TestGetAverage:
    """Tests for get_average(nums)."""

    @pytest.mark.parametrize(
        ("nums", "expected"),
        [
            ([1, 2, 3, 4], 2.5),
            ([5], 5.0),
            ([-2, -4, -6], -4.0),
            ([1.5, 2.5, 3.0], 2.3333333333333335),
            ([10, 10, 10], 10.0),
            ((1, 2, 3), 2.0),
        ],
        ids=[
            "integers",
            "single-element",
            "all-negative",
            "floats",
            "all-equal",
            "tuple-input",
        ],
    )
    def test_normal_cases(self, nums, expected):
        assert get_average(nums) == pytest.approx(expected)

    @pytest.mark.parametrize("nums", [[], ()])
    def test_empty_sequence_raises(self, nums):
        with pytest.raises(ValueError, match="Cannot compute average of an empty sequence"):
            get_average(nums)

    def test_large_sequence(self):
        nums = list(range(1, 101))
        assert get_average(nums) == pytest.approx(50.5)


class TestFindMax:
    """Tests for find_max(items)."""

    @pytest.mark.parametrize(
        ("items", "expected"),
        [
            ([3, 1, 4, 1, 5], 5),
            ([9], 9),
            ([-5, -1, -10], -1),
            ([0, 0, 0], 0),
            ([2, 2, 7, 7], 7),
            (("a", "m", "z"), "z"),
        ],
        ids=[
            "typical-list",
            "single-element",
            "negative-numbers",
            "all-equal",
            "duplicates",
            "string-tuple",
        ],
    )
    def test_normal_cases(self, items, expected):
        assert find_max(items) == expected

    @pytest.mark.parametrize(
        ("items", "expected"),
        [
            ([9, 1, 3, 5], 9),
            ([1, 9, 3, 5], 9),
        ],
        ids=["max-at-start", "max-at-middle"],
    )
    def test_max_position(self, items, expected):
        assert find_max(items) == expected

    @pytest.mark.parametrize("items", [[], ()])
    def test_empty_sequence_raises(self, items):
        with pytest.raises(ValueError, match="Cannot find max of an empty sequence"):
            find_max(items)


class TestMainBlock:
    """Smoke test for the module's __main__ demo block."""

    def test_main_runs_without_traceback(self):
        result = subprocess.run(
            [sys.executable, str(MODULE_PATH)],
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0
        assert "divide(10, 0) failed: Cannot divide by zero" in result.stdout
        assert "get_average([]) failed: Cannot compute average of an empty sequence" in result.stdout
        assert "find_max([]) failed: Cannot find max of an empty sequence" in result.stdout
        assert "Traceback" not in result.stderr
