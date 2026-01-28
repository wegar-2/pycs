from __future__ import annotations
from typing import Any, Final, Optional


class LinkedListNode:

    def __init__(
            self,
            key: int,
            value: Optional[Any] = None,
            nxt: Optional[LinkedListNode] = None,
            prv: Optional[LinkedListNode] = None,
    ):
        self._key: Final[int] = key
        self._value: Any = value
        self._nxt: Optional[LinkedListNode] = nxt
        self._prv: Optional[LinkedListNode] = prv

    @property
    def key(self) -> int:
        return self._key

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value: Any):
        self._value = value

    @property
    def next(self) -> LinkedListNode:
        return self._nxt

    @next.setter
    def next(self, nxt: LinkedListNode) -> None:
        self._nxt = nxt

    @property
    def prev(self) -> LinkedListNode | None:
        return self._prv

    @prev.setter
    def prev(self, prv: LinkedListNode):
        self._prv = prv

    def __str__(self) -> str:
        return f"LinkedListNode(key={self._key}, value{self._value}, ...)"
