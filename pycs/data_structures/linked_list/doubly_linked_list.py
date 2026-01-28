from pycs.data_structures.linked_list.linked_list_node import LinkedListNode
from pycs.data_structures.linked_list.linked_list import LinkedList


class DoublyLinkedList(LinkedList):

    def get_keys(self) -> list[int]:
        keys: list[int] = []
        node = self._first_node
        while node.next is not None:
            keys.append(node.key)
        return keys

    def append(self, node: LinkedListNode):
        node.next = None
        if self._size == 0:
            node.next = None
            node.prev = None
            self._first_node = node
            self._last_node = node
        else:
            node.prev = self._last_node
            self._last_node.next = node
            self._last_node = node
        self._size += 1

    def pop_right(self) -> LinkedListNode | None:
        if self._size == 0:
            return None
        elif self._size == 1:
            node = self._first_node
            self._first_node = None
            self._last_node = None
            self._size -= 1
            return node
        else:
            node = self._last_node
            self._last_node = self._last_node.prev
            node.prev = None
            self._size -= 1
            return node

    def pop_left(self) -> LinkedListNode | None:
        if self._size == 0:
            return None
        else:
            node = self._first_node
            self._first_node = node.next
            self._first_node.prev = None
            self._size -= 1
            node.next = None
            return node

    def insert(self, idx: int, node: LinkedListNode) -> None:
        if idx == 0:
            node.next = self._first_node
            self._first_node = node
            self._size += 1
        elif idx == self._size:
            self.append(node)
        elif 1 <= idx <= self._size - 1:
            prev_node, curr_node = self._first_node, self._first_node.next
            i = 1
            while curr_node.next is not None:
                if idx == i:
                    curr_node.prev = node
                    node.next = curr_node
                    prev_node.next = node
                    node.prev = prev_node
                    break
                prev_node, curr_node = curr_node, curr_node.next
                i += 1
            self._size += 1
        else:
            raise IndexError(
                f"Trying to insert into index {idx} which is behind end of "
                f"sll of length {self._size}"
            )

    def remove(self, idx: int) -> LinkedListNode:
        self._validate_list_index(idx=idx)
        if idx == 0:
            self._first_node = self._first_node.next
            self._size -= 1
            return self._first_node
        else:
            prev_node, curr_node = self._first_node, self._first_node.next
            for i in range(1, idx + 1):
                curr_node = curr_node.next
                prev_node = curr_node
            prev_node.next = curr_node.next
            self._size -= 1
            return curr_node

    def __setitem__(self, idx, node: LinkedListNode) -> None:
        self._validate_list_index(idx)
        node.prev = None
        if idx == 0:
            node.next = self._first_node.next
            self._first_node = node
        else:
            prev_node = self._first_node
            curr_node = prev_node.next
            for i in range(1, idx + 1):
                if idx == i:
                    node.next = curr_node.next
                    prev_node.next = node
                    break
                prev_node, curr_node = curr_node, curr_node.next
