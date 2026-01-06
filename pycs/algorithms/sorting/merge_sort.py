from typing import Optional


__all__ = ["merge_sort"]


def _merge(left: list[int], right: list[int], nums: list[int]) -> None:
    i, j = 0, 0
    while i + j < len(nums):
        if j == len(right) or (i < len(left) and left[i] < right[j]):
            nums[i + j] = left[i]
            i += 1
        else:
            nums[i + j] = right[j]
            j += 1


def merge_sort(
        nums: list[int]
) -> None:
    if len(nums) < 2:
        return

    mid: int = len(nums) // 2
    left_nums: list[int] = nums[:mid]
    right_nums: list[int] = nums[mid:]

    merge_sort(nums=left_nums)
    merge_sort(nums=right_nums)
    _merge(left=left_nums, right=right_nums, nums=nums)


if __name__ == "__main__":
    from pycs.common.testing import array_for_sorting
    import copy
    ar = array_for_sorting()
    ar_cp = copy.deepcopy(ar)
    merge_sort(nums=ar)
    ar_srtd = sorted(ar_cp)

    print(ar_srtd == ar)
