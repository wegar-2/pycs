from __future__ import annotations
from typing import Optional


class Node:

    def __init__(self, value: int):
        self._value: int = value
        self._next_node: Optional[Node] = None

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value

    @property
    def next_node(self) -> Node:
        return self._next_node

    @next_node.setter
    def next_node(self, next_node: Node):
        self._next_node = next_node
    