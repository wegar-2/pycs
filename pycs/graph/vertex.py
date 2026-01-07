from typing import Any


class Vertex:

    __slots__ = "_element"

    def __init__(self, element: Any):
        self._element = element

    @property
    def element(self) -> Any:
        return self._element

    def __hash__(self) -> int:
        return hash(id(self))
