from calc import mean, median


def test_mean_basic():
    assert mean([2, 4, 6]) == 4.0


def test_mean_single():
    assert mean([7]) == 7.0


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5
