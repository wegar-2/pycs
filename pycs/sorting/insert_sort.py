

def insert_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums), 1):
        value: int = nums[i]
        j = i
        while j > 0 and value < nums[j-1]:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = value
    return nums
