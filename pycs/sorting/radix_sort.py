from array import array

from pycs.nt.common import digit_at_base


def _counting_sort_at_base10(ar: array, digit_from_right: int) -> array:

    sorted_ar: array = array("i", [0] * len(ar))
    counts_ar: array = array("i", [0] * 10)

    digits_ar: array = array("i", [
        digit_at_base(n=x, b=10, i=digit_from_right) for x in ar
    ])

    for digit in digits_ar:
        counts_ar[digit] += 1
    for i in range(1, 10, 1):
        counts_ar[i] = counts_ar[i] + counts_ar[i-1]

    for i in reversed(range(len(ar))):
        sorted_ar[counts_ar[digits_ar[i]] - 1] = ar[i]
        counts_ar[digits_ar[i]] -= 1

    return sorted_ar


def radix_sort(nums: list[int]) -> list[int]:
    ar_nums: array = array("i", nums)
    base10_max_len: int = max([len(str(x)) for x in nums])
    for digit in range(1, base10_max_len + 1, 1):
        ar_nums = _counting_sort_at_base10(ar=ar_nums, digit_from_right=digit)
    return list(ar_nums)
