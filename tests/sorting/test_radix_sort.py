from pycs.common.testing import array_for_sorting
from pycs.sorting.radix_sort import radix_sort


def test_radix_sort():
    for k in range(100):
        nums = array_for_sorting()
        assert sorted(nums) == radix_sort(nums)
