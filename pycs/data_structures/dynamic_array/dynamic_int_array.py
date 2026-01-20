from array import array


class DynamicArray:

    def __init__(self):
        self._data: array = array("i", [0])

    def __len__(self) -> int:
        return len(self._data)

    def insert(self):
        pass

    def append(self, i: int):
        pass
