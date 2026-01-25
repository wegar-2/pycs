

class Heap:

    def __init__(self):
        self._data: list[int] = []

    @property
    def data(self) -> list[int]:
        return self._data

    def __len__(self) -> int:
        return len(self._data)

    def _down_heap_bubble(self, idx: int = 0) -> None:
        curr_idx: int = idx
        value: int = self._data[curr_idx]

        lc_idx = self._index_left_child(idx=curr_idx)
        rc_idx = self._index_right_child(idx=curr_idx)

        if lc_idx <= len(self) - 1:
            lc_value = self._data[lc_idx]
            if lc_value < value:
                self._data[lc_idx], self._data[curr_idx] = (
                    self._data[curr_idx], self._data[lc_idx])
                self._down_heap_bubble(idx=lc_idx)
            else:
                return None

        if rc_idx <= len(self) - 1:
            rc_value = self._data[rc_idx]
            if rc_value < value:
                self._data[rc_idx], self._data[curr_idx] = (
                    self._data[curr_idx], self._data[rc_idx])
                self._down_heap_bubble(idx=rc_idx)
            else:
                return None

        return None

    def _up_heap_bubble(self):

        last_idx: int = len(self._data) - 1
        curr_idx: int = last_idx
        value: int = self._data[curr_idx]

        while curr_idx > 0:
            parent_idx = (curr_idx - 1) // 2
            if (parent_value := self._data[parent_idx]) > value:
                self._data[parent_idx], self._data[curr_idx] = (
                    value, parent_value)
                curr_idx = parent_idx
            else:
                break

    def append(self, x: int) -> None:
        self._data.append(x)
        self._up_heap_bubble()

    def pop(self) -> int:
        if len(self._data) == 0:
            raise ValueError("Heap is empty! ")
        last: int = self._data.pop()

        if len(self._data) == 0:
            return last

        first: int = self._data[0]
        self._data[0] = last
        self._down_heap_bubble()
        return first

    def peek_min(self) -> int:
        if len(self) == 0:
            raise ValueError("Heap is empty! ")
        return self._data[0]

    @staticmethod
    def _index_parent(idx: int) -> int | None:
        if idx == 0:
            return None
        return (idx - 1) // 2

    @staticmethod
    def _index_left_child(idx: int) -> int:
        return 2 * idx + 1

    @staticmethod
    def _index_right_child(idx: int) -> int:
        return 2 * idx + 2
