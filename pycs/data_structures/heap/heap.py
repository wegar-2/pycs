

class Heap:

    def __init__(self):
        self._data: list[int] = []

    def __len__(self) -> int:
        return len(self._data)

    def _bubble_up(self):
        pass

    def append(self, x: int) -> None:
        self._data.append(x)

    @property
    def peek_min(self) -> int:
        return self._data[0]

    def pop_min(self) -> int:
        pass

    def _index_parent(self, idx: int) -> int | None:
        pass

    def _index_left_child(self, idx: int) -> int:
        pass

    def _index_right_child(self, idx: int) -> int:
        pass
