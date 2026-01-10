from __future__ import annotations
from typing import Union


class Vertex:

    __slots__ = "_element"

    def __init__(self, element: Union[int, str]):
        self._element = element

    @property
    def element(self) -> Union[int, str]:
        return self._element

    def __hash__(self) -> int:
        return hash(self._element)

    def __eq__(self, other: Vertex) -> bool:
        return self._element == other.element
