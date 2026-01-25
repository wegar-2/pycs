from pycs.data_structures.heap.heap import Heap


def heap_sort(nums: list[int]) -> list[int]:
    h = Heap()
    for x in nums:
        h.append(x)
    res = []
    for _ in range(len(nums)):
        res.append(h.pop())
    return res
