from __future__ import annotations
from typing import Any, Optional

from pycs.graph.vertex import Vertex


class Edge:

    __slots__ = "_origin", "_destination", "_element"

    def __init__(self, o: Vertex, d: Vertex, element: Optional[Any] = None):
        self._origin: Vertex = o
        self._destination: Vertex = d
        self._element: Any = element

    @property
    def endpoints(self) -> tuple[Vertex, Vertex]:
        return self._origin, self._destination

    @property
    def origin(self) -> Vertex:
        return self._origin

    @property
    def destination(self) -> Vertex:
        return self._destination

    @property
    def element(self) -> Any:
        return self._element

    def opposite(self, v: Vertex) -> Vertex:
        return self._origin if v == self._destination else self._destination

    def __eq__(self, other: Edge) -> bool:
        return self._origin