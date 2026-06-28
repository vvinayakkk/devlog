def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def get_average(nums):
    if not nums:
        raise ValueError("Cannot compute average of an empty sequence")
    return sum(nums) / len(nums)


def find_max(items):
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
