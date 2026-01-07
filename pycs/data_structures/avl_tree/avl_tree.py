import logging
from typing import Optional

from pycs.data_structures.avl_tree.node import Node

__all__ = ["AVLTree"]

logger = logging.getLogger(__name__)


class AVLTree:

    def __init__(self):
        self.root: Optional[Node] = None

    @staticmethod
    def _node_height(node: Optional[Node]) -> int | None:
        return node.height if node is not None else 0

    @staticmethod
    def _node_balance(node: Node) -> int:
        return (
                AVLTree._node_height(node=node.left) -
                AVLTree._node_height(node=node.right)
        )

    def _insert(self, node: Optional[Node], key: int) -> Node:
        if node is None:
            return Node(key=key)

        if key < node.key:
            node.left = self._insert(node=node.left, key=key)
        elif key > node.key:
            node.right = self._insert(node=node.right, key=key)
        else:
            logger.info(f"Node with key {key} already exists! ")

        node.height = 1 + max(
            self._node_height(node=node.left),
            self._node_height(node=node.right)
        )

        balance: int = self._node_balance(node=node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node=node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node=node.left)
            return self._right_rotate(node=node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node=node.right)
            return self._left_rotate(node=node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node=node)

        return node

    def insert(self, key: int):
        self.root = self._insert(node=self.root, key=key)

    def _right_rotate(self, node: Node) -> Node:
        z = node
        y = node.left
        t3 = y.right
        if t3 is not None:
            print(f"{self._node_height(node=t3)=}")

        z.left = t3
        y.right = z

        z.height = 1 + max(
            self._node_height(z.left), self._node_height(node=z.right)
        )
        y.height = 1 + max(
            self._node_height(y.left), self._node_height(node=y.right)
        )

        return y

    def _left_rotate(self, node: Node) -> Node:
        z = node
        y = node.right
        t2 = y.left
        if t2 is not None:
            print(f"{self._node_height(node=t2)=}")

        z.right = t2
        y.left = z

        z.height = 1 + max(
            self._node_height(z.left), self._node_height(node=z.right)
        )
        y.height = 1 + max(
            self._node_height(y.left), self._node_height(node=y.right)
        )

        return y

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


if __name__ == "__main__":

    nums = [10, 8, 1, 9, 11, 15, 12, 13, 17, 2, 99, 7, 6, 3, 5, 4, 32, 45, 33]

    tree = AVLTree()

    for x in nums:
        tree.insert(key=x)

    print(f"{tree.inorder()=}")
