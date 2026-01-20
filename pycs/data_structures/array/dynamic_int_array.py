from array import array
import logging


logger = logging.getLogger(__name__)


class DynamicIntArray:

    def __init__(self, size: int = 1):
        self._size: int = size
        self._memory_size: int = 2 ** size.bit_length()
        self._data: array = array("i", [0] * self._memory_size)

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, item: int) -> int:
        if item >= self._size:
            raise IndexError("")
        return self._data[item]

    def __setitem__(self, key: int, value: int) -> None:
        if key >= self._size:
            raise IndexError("")
        self._data[key] = value

    def append(self, value: int) -> None:
        pass

    def pop(self) -> int | None:
        pass

    def _enlarge(self):
        pass

    def _shrink(self):
        pass
