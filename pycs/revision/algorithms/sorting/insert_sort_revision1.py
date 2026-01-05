

def insert_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums), 1):
        cur: int = nums[i]
        j = i - 1
        while j > 0 and cur > nums[j]:
            nums[j] = nums[j+1]
        nums[j] = cur
    return nums


if __name__ == "__main__":
    pass
