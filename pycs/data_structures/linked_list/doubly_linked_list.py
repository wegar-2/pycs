from pycs.data_structures.linked_list.linked_list_node import LinkedListNode


class DoublyLinkedList:

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

    def get_keys(self) -> list[int]:
        keys: list[int] = []
        node = self._first_node
        while node.next is not None:
            keys.append(node.key)
        return keys

    def __len__(self) -> int:
        return self._size

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

    def _validate_list_index(self, idx: int) -> None:
        if self._size == 0:
            raise IndexError(
                f"Trying to access index {idx} of an empty array! ")
        else:
            if not 0 <= idx <= (last_correct_idx := self._size - 1):
                raise IndexError(
                    f"Trying to access index {idx} - the index is out of the "
                    f"range of valid indexes [0, ..., {last_correct_idx}]"
                )

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
                    node.next = curr_node
                    prev_node.next = node
                    break
                prev_node, curr_node = curr_node, curr_node.next
                i += 1
            self._size += 1
        else:
            raise IndexError(
                f"Trying to insert into index {idx} which is behind end of "
                f"sll of length {self._size}"
            )


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

    def __contains__(self, key: int) -> bool:
        if self._size == 0:
            return False
        else:
            node = self._first_node
            while node.next is not None:
                if node.key == key:
                    return True
                node = node.next
            if key == node.key:
                return True
            return False
