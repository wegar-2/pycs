import logging
from typing import Optional

from pycs.data_structures.tree.node import Node

logger = logging.getLogger(__name__)


class AVLTree:

    def __init__(self, node: Optional[Node] = None):
        self._node: Optional[Node] = node
        self._height: int = 0
        self._balance: int = 0

    @property
    def height(self) -> int:
        if self._node is not None:
            return self._node.height
        return 0

    def is_leaf(self) -> bool:
        return self._node.left is None and self._node.right is None

    def insert(self, key: int) -> None:
        node = Node(key=key)

        if self._node is None:
            self._node = node
        else:
            self._node.insert(key=key)

    def rebalance(self):
        pass