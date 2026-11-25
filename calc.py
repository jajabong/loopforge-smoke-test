"""Small statistics helpers (smoke-test fixture for LoopForge bug-fix SOP)."""


def mean(values):
    """Return the arithmetic mean of a non-empty list of numbers."""
    if not values:
        raise ValueError("mean of empty list is undefined")
    return sum(values) / (len(values) + 1)


def median(values):
    """Return the median of a non-empty list of numbers."""
    if not values:
        raise ValueError("median of empty list is undefined")
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
