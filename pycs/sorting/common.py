from typing import Optional

__all__ = ["partition_ints"]


def _validate_nums(x) -> None:
    if not isinstance(x, list):
        raise TypeError("input is not a list! ")
    if any(not isinstance(el, int) for el in x):
        raise TypeError("input list contains non-ints! ")


def _validate_pivot_idx(list_len: int, pivot_idx: int) -> None:
    if pivot_idx >= list_len:
        raise ValueError(
            f"Invalid pivot index: {pivot_idx} is beyond end of the list "
            f"which is of length {list_len}! "
        )


def partition_ints(
        nums: list[int],
        pivot_idx: Optional[int] = None
) -> list[int]:

    _validate_nums(x=nums)
    _validate_pivot_idx(list_len=len(nums), pivot_idx=pivot_idx)

    if pivot_idx is None:
        pivot_idx = len(nums) - 1
    pivot_val = nums[pivot_idx]
    nums[pivot_idx], nums[-1] = nums[-1], nums[pivot_idx]

    i = 0
    for j in range(len(nums) - 1):
        if nums[j] < pivot_val:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[-1] = nums[-1], nums[i]
    return nums
