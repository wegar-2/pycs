from pycs.data_structures.linked_list.linked_list_node import LinkedListNode


class LinkedList:

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

    def __len__(self) -> int:
        return self._size

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

    def __getitem__(self, idx: int) -> LinkedListNode:
        self._validate_list_index(idx)
        node = self._first_node
        for i in range(1, idx + 1):
            node = node.next
        return node

    def get_keys(self) -> list[int]:
        keys: list[int] = []
        node = self._first_node
        while node.next is not None:
            keys.append(node.key)
        return keys
