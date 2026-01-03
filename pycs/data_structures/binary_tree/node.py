from __future__ import annotations
from typing import Optional
from itertools import chain


class Node:

    def __init__(self, value: int):
        self._value: int = value
        self._left_child: Optional[Node] = None
        self._right_child: Optional[Node] = None

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value

    @property
    def left_child(self) -> Optional[Node]:
        return self._left_child

    @left_child.setter
    def left_child(self, child: Node):
        self._left_child = child

    @property
    def right_child(self) -> Optional[Node]:
        return self._right_child

    @right_child.setter
    def right_child(self, child: Node):
        self._right_child = child

    def insert(self, value: int):
        if value <= self._value:
            if self._left_child is None:
                self._left_child = Node(value=value)
            else:
                self._left_child.insert(value=value)
        else:
            if self._right_child is None:
                self._right_child = Node(value=value)
            else:
                self._right_child.insert(value=value)

    def get_sorted_values(self) -> list[int]:
        lists_out = []
        if self._left_child is not None:
            lists_out.append(self._left_child.get_sorted_values())
        lists_out.append([self._value])
        if self._right_child is not None:
            lists_out.append(self._right_child.get_sorted_values())
        return list(chain.from_iterable(lists_out))


if __name__ == "__main__":
    print(list(chain([1, 2], [2], [33, 123])))


