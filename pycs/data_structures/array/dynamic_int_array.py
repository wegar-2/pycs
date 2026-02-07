from array import array
import logging
from typing import Final


logger = logging.getLogger(__name__)


class DynamicIntArray:

    _ENLARGE_MULTIPLIER: Final[float] = 2
    _SHRINK_MULTIPLIER: Final[float] = 0.25

    def __init__(self, size: int = 1):
        self._size: int = size
        self._memory_size: int = 2 ** size.bit_length()
        self._data: array = array("i", [0] * self._memory_size)

    def _validate_idx(self) -> None:
        pass

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, idx: int) -> int:
        if idx >= self._size:
            raise IndexError("")
        return self._data[idx]

    def __setitem__(self, idx: int, value: int) -> None:
        if idx >= self._size:
            raise IndexError("")
        self._data[idx] = value

    def append(self, value: int) -> None:
        pass

    def pop(self) -> int | None:
        pass

    def _enlarge(self):
        new_array = array("i")

    def _shrink(self):
        pass
