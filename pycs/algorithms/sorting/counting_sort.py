from array import array

__all__ = ["counting_sort"]


def _validate_input(nums: list[int]) -> None:
    if not all(isinstance(x, int) and x >= 0 for x in nums):
        raise ValueError("Not all elements of input to counting_sort "
                         "are nonnegative integers! ")


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

    counts_arr: array = array("i", [0] * (m + 1))
    sorted_arr: array = array("i", [0] * len(nums_ar))

    for x in nums_ar:
        counts_arr[x] += 1
    for i in range(1, len(counts_arr)):
        counts_arr[i] = counts_arr[i-1] + counts_arr[i]

    for x in nums_ar[::-1]:
        sorted_arr[counts_arr[x]-1] = x
        counts_arr[x] -= 1

    return sorted_arr


if __name__ == "__main__":
    import random


    def _generate_nums(len_: int = 10_000, upper_bound: int = 1_000) -> list[
        int]:
        random.seed(123)
        return [random.randint(a=1, b=upper_bound) for _ in range(len_)]


    nums = _generate_nums()
    assert sorted(nums) == list(counting_sort(nums))
