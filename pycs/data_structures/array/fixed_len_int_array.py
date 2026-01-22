from typing import Final


class FixedLenIntArray:
    """
    Note: since __getitem__ is implemented this class is iterable
    """

    def __init__(self, len_: int):
        self._validate_is_positive_int(i=len_)
        self._l: Final[int] = len_
        self._data: list[int] = [0] * len_

    @property
    def data(self):
        return self._data

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
            raise IndexError(f"Invalid array index {i} for array of length "
                             f"{self._l}")
