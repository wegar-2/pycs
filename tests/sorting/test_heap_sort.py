from pycs.common.testing import array_for_sorting
from pycs.sorting.heap_sort import heap_sort


def test_radix_sort():
    for k in range(100):
        nums = array_for_sorting()
        assert sorted(nums) == heap_sort(nums)
