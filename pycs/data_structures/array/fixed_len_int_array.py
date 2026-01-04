from typing import Final


class FixedLenIntArray:

    def __init__(self, l: int):
        self._validate_is_positive_int(i=l)
        self._l: Final[int] = l
        self._data: list[int] = [0] * l

    def __len__(self) -> int:
        return self._l

    def __setitem__(self, key: int, value: int) -> None:
        self._is_valid_array_index(i=key)
        self._is_valid_array_value(v=value)
        self._data[key] = value

    def __getitem__(self, item: int) -> int:
        self._is_valid_array_index(i=item)
        return self._data[item]

    @staticmethod
    def _validate_is_positive_int(i: int) -> None:
        if i <= 0:
            raise Exception(f"Number {i=} is not a positive integer!")

    @staticmethod
    def _is_valid_array_value(v: int) -> None:
        if not isinstance(v, int):
            raise ValueError(f"{v=} is not an int! ")

    def _is_valid_array_index(self, i: int) -> None:
        if i < 0 or i >= self._l:
            raise IndexError(f"")

    def __iter__(self):
        pass
