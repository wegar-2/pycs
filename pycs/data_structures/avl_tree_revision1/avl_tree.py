import logging
from typing import Optional

from pycs.data_structures.avl_tree_revision1.node import Node

logger = logging.getLogger(__name__)


class AVLTree:

    def __init__(self):
        self.root: Optional[Node] = None

    @staticmethod
    def _node_height(node: Optional[Node]) -> int:
        return 0 if node is None else node.height

    def _node_balance(self, node: Node) -> int:
        return (
            self._node_height(node=node.left) -
            self._node_height(node=node.right)
        )

    def insert(self, key: int):
        self.root = self._insert_into_node(node=self.root, key=key)

    def _insert_into_node(self, node: Node | None, key: int) -> Node:
        if node is None:
            return Node(key=key)
        else:

            if key < node.key:
                node.left = self._insert_into_node(node=node.left, key=key)
            elif key > node.key:
                node.right = self._insert_into_node(node=node.right, key=key)
            else:
                logger.info(f"Value of key: {key} already present in the node...")

            node.height = max(
                self._node_height(node=node.left),
                self._node_height(node=node.right)
            ) + 1

            balance = self._node_balance(node=node)

            if balance > 1 and key < node.left.key:
                return self._right_rotate(node=node)
            elif balance > 1 and key > node.left.key:
                node.left = self._left_rotate(node=node.left)
                return self._right_rotate(node=node)
            elif balance < -1 and key > node.right.key:
                return self._left_rotate(node=node)
            elif balance < -1 and key < node.right.key:
                node.right = self._right_rotate(node=node.right)
                return self._left_rotate(node=node)

            return node


    def _left_rotate(self, node: Node) -> Node:

        z = node
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        y.height = max(
            self._node_height(node=y.left),
            self._node_height(node=y.right)
        ) + 1
        z.height = max(
            self._node_height(node=z.left),
            self._node_height(node=z.right)
        ) + 1
        return y

    def _right_rotate(self, node: Node) -> Node:

        z = node
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        y.height = max(
            self._node_height(node=y.left),
            self._node_height(node=y.right)
        ) + 1
        z.height = max(
            self._node_height(node=z.left),
            self._node_height(node=z.right)
        ) + 1

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
