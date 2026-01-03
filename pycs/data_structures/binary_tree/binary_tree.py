from pycs.data_structures.binary_tree.node import Node


class BinaryTree:

    def __init__(self, value: int):
        self._root: Node = Node(value=value)

    def insert(self, value: int):
        self._root.insert(value=value)

    def get_sorted_values(self) -> list[int]:
        return self._root.get_sorted_values()


if __name__ == "__main__":
    bt = BinaryTree(value=123)
    bt.insert(1222)
    bt.insert(27)
    bt.insert(90)
    bt.insert(2002)
    bt.insert(1)
    bt.insert(111)
    bt.insert(111)
    print(bt.get_sorted_values())
