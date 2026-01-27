from pycs.data_structures.linked_list.linked_list_node import LinkedListNode


class SinglyLinkedList:

    def __init__(self):
        self._first_node: LinkedListNode | None = None
        self._last_node: LinkedListNode | None = None
        self._size: int = 0

    @property
    def first_node(self) -> LinkedListNode | None:
        return self._first_node

    @property
    def last_node(self) -> LinkedListNode | None:
        return self._last_node

    def __len__(self) -> int:
        return self._size

    def append(self, node: LinkedListNode):
        if self._size == 0:
            node.prev = None
            node.next = None
            self._first_node = node
            self._last_node = node
        else:
            node.next = None
            self._last_node.next = node
        self._size += 1

    def pop_right(self) -> LinkedListNode | None:
        if self._size == 0:
            return None
        else:
            node = self._first_node
            next_node = self._first_node.next
            while next_node is not None:
                node = next_node
                next_node = node.next
            self._size -= 1
            return node

    def pop_left(self) -> LinkedListNode | None:
        if self._size == 0:
            return None
        else:
            node = self._first_node
            self._first_node = node.next
            self._size -= 1
            return node

    def _validate_list_index(self, idx: int) -> None:
        if self._size == 0:
            raise IndexError()
        else:
            if not 0 <= idx <= self._size - 1:
                raise IndexError()

    def insert(self, idx: int, node: LinkedListNode) -> None:
        self._validate_list_index(idx=idx)
        if idx == 0:
            node.next = self._first_node
            self._first_node = node
        else:
            prev_node, curr_node = self._first_node, self._first_node.next
            i = 1
            while curr_node.next is not None:
                if idx == i:
                    node.next = curr_node
                    prev_node.next = node
                    break
                prev_node, curr_node = curr_node, curr_node.next
                i += 1
        self._size += 1

    def remove(self, idx: int) -> LinkedListNode: # noqa
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

    def __getitem__(self, idx: int) -> LinkedListNode:
        self._validate_list_index(idx)
        node = self._first_node
        for i in range(1, idx + 1):
            node = node.next
        return node

    def __setitem__(self, idx, node: LinkedListNode) -> None:
        self._validate_list_index(idx)
        self._validate_list_index(idx=idx)
        if idx == 0:
            node.next = self._first_node.next
            self._first_node = node
        else:
            prev_node, curr_node = self._first_node, self._first_node.next
            i = 1
            while curr_node.next is not None:
                if idx == i:
                    node.next = curr_node.next
                    prev_node.next = node
                    break
                prev_node, curr_node = curr_node, curr_node.next

    def __contains__(self, key: int) -> bool:
        if self._size == 0:
            return False
        else:
            node = self._first_node
            while node.next is not None:
                if node.key == key:
                    return True
                node = node.next
            return False
