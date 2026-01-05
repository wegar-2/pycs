

def insert_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums), 1):
        cur: int = nums[i]
        j = i
        while j > 0 and cur < nums[j-1]:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = cur
    return nums


if __name__ == "__main__":
    from pycs.common.testing import array_for_sorting
    nums: list[int] = array_for_sorting()
    res1 = sorted(nums)
    res2 = insert_sort(nums)

    print(res1 == res2)
