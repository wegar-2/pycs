from array import array

__all__ = ["counting_sort"]


def _validate_input(nums: list[int]) -> None:
    if not all(isinstance(x, int) and x >=0 for x in nums):
        raise ValueError(f"")


def _max(nums: list[int]) -> int:
    m: int = nums[0]
    for x in nums[1:]:
        if x > m:
            m = x
    return m


def counting_sort(nums: list[int], limit_multiplier: int = 100):

    _validate_input(nums)
    nums_ar: array = array("i", nums)
    m: int = _max(nums)

    if m > limit_multiplier * len(nums):
        pass

    b_arr: array = array("i", [0] * m)
    c_arr: array = array("i", [0] * len(nums))

    for x in nums:
        b_arr[x] += 1
    for i in range(1, len(b_arr)):
        b_arr[i] = b_arr[i-1] + b_arr[i]

    for x in nums_ar[::-1]:
        c_arr[b_arr[x]] = x
        b_arr[x] -= 1

    return c_arr
