from pycs.algorithms.sorting.counting_sort import counting_sort

import random

from pytest import raises

def _generate_nums(len_: int = 10_000, upper_bound: int = 1_000) -> list[int]:
    random.seed(123)
    return [random.randint(a=1, b=upper_bound) for _ in range(len_)]


def test_counting_sort():
    nums = _generate_nums()
    assert sorted(nums) == list(counting_sort(nums))


def test_raises_error_on_negative_numbers():
    nums = _generate_nums()
    nums[50] = -123
    with raises(ValueError):
        counting_sort(nums)


def test_input_too_large_elements():
    nums = _generate_nums(len_=20, upper_bound=100_000)
    with raises(ValueError):
        counting_sort(nums)
