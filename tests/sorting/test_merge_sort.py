from copy import deepcopy

from pycs.sorting.merge_sort import merge_sort
from pycs.common.testing import array_for_sorting


def test_merge_sort():
    for k in range(100):
        ar = array_for_sorting()
        ar_copy = deepcopy(ar)
        ar_sorted = sorted(ar_copy)
        merge_sort(nums=ar)
        assert ar_sorted == ar
