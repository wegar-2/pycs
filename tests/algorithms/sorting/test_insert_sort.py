from pycs.algorithms.sorting.insert_sort import insert_sort
from pycs.common.testing import array_for_sorting


def test_insert_sort():
    for k in range(100):
        nums = array_for_sorting()
        nums_is = insert_sort(nums=nums)
        nums_bi = sorted(nums)
        assert nums_bi == nums_is
