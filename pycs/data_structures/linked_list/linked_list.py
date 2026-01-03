from typing import Optional
from pycs.data_structures.linked_list.node import Node


class LinkedList:

    def __init__(self):
        self._first_node: Optional[Node] = None
        self._last_node: Optional[Node] = None

    def add_node(self, value: int):
        if self._first_node is None:
            self._first_node = Node(value=value)
            self._last_node = self._first_node
        else:
            node = Node(value=value)
            self._last_node.next_node = node
            self._last_node = node

    def insert_node(self, value: int, position: int):
        pass

    def __len__(self) -> int:
        node = self._first_node

    def pop(self):
        pass

    def get_node(self, position: int) -> Node:
        pass


if __name__ == "__main__":
    pass
