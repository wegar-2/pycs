from array import array

from pycs.algorithms.sorting.counting_sort import counting_sort


def _counting_sort(nums: list[int], digit: int) -> array:

    ar: array = array("i", nums)
    ar_max: int = max(ar)

    sorted_ar: array = array("i", [0] * len(ar))
    counts_ar: array = array("i", range(ar_max + 1))

    digits_ar: array = array("i", ar)

    # for i

    return sorted_ar


def _matrix_based_radix_sort(nums: list[int]) -> list[int]:
    pass


def _radix_sort(nums: list[int]) -> list[int]:
    pass


def radix_sort(nums: list[int]) -> list[int]:

    base10_max_len: int = max([len(str(x)) for x in nums])
    str_nums: list[str] = [str(x).rjust(base10_max_len, "0") for x in nums]

    return nums


def radix_sort_base10(nums: list[int]) -> list[int]:
    base10_max_len: int = max([len(str(x)) for x in nums])

    ar_nums: array = array("i", nums)




    return nums
