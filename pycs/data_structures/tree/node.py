from __future__ import annotations
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class Node:

    def __init__(
            self,
            key: int,
            parent: Optional[Node] = None,
            left: Optional[Node] = None,
            right: Optional[Node] = None
    ):
        self._key: int = key
        self._parent: Optional[Node] = parent
        self._left: Optional[Node] = left
        self._right: Optional[Node] = right
        self._height: int = 0

    @property
    def key(self) -> int:
        return self._key

    @key.setter
    def key(self, key: int):
        self._key = key

    @property
    def parent(self) -> Node | None:
        return self._parent

    @parent.setter
    def parent(self, parent: Optional[Node]) -> None:
        self._parent = parent

    @property
    def left(self) -> Node | None:
        return self._left

    @left.setter
    def left(self, left: Optional[Node]) -> None:
        self._left = left

    @property
    def right(self) -> Node | None:
        return self._right

    @right.setter
    def right(self, right: Optional[Node]) -> None:
        self._right = right

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        self._height = height

    def is_leaf(self) -> bool:
        return self._left is None and self._right is None

    def insert(self, key: int):
        if self._key < key:
            if self._left is None:
                self._left = Node(key=key, parent=self)
                self._left.update_height(recursive=True)
            else:
                self._left.insert(key=key)
        elif self._key > key:
            if self._right is None:
                self._right = Node(key=key, parent=self)
                self._right.update_height(recursive=True)
            else:
                self._right.insert(key=key)
        else:
            logger.info(f"Key {key} already present in the tree")
            # no need to recalculate heights here

    def update_height(
            self,
            recursive: bool = True,
            update_from_left: bool = True
    ) -> None:
        if not self.is_leaf():
            raise Exception("Invalid update height call! ")
        if self.is_leaf():
            pass
        else:
            if update_from_left:
                if self._left.height + 1 <= self._right._height:
                    pass
                else:
                    self._height += 1
            else:
                pass
        if recursive:
            parent = self._parent
            while parent is not None:
                parent.update_height(
                    recursive=True,
                    update_from_left=self._parent.left is self
                )
                parent = parent.parent
