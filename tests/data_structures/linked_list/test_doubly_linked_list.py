from pytest import fixture

from pycs.data_structures.linked_list.linked_list_node import LinkedListNode
from pycs.data_structures.linked_list.doubly_linked_list import (
    DoublyLinkedList)


@fixture
def default_dll() -> DoublyLinkedList:
    first, second, last = (
        LinkedListNode(1), LinkedListNode(22), LinkedListNode(333))
    sll = DoublyLinkedList()
    sll.append(first)
    sll.append(second)
    sll.append(last)
    return sll


def test_first_last_node_and_len():

    sll = DoublyLinkedList()
    assert len(sll) == 0
    first = LinkedListNode(key=22)

    sll.append(first)
    assert len(sll) == 1
    assert sll.first_node == first
    assert sll.last_node == first

    second = LinkedListNode(key=333)
    sll.append(second)
    assert len(sll) == 2
    assert sll.first_node == first
    assert sll.last_node == second

    last = LinkedListNode(444)
    sll.append(last)
    assert len(sll) == 3
    assert sll.first_node == first
    assert sll.last_node == last


def test_append(default_dll):
    new_node = LinkedListNode(4444)
    default_dll.append(new_node)
    assert len(default_dll) == 4
    assert default_dll.last_node == new_node


def test_pop_left(default_dll):

    first_node = default_dll.pop_left()
    assert len(default_dll) == 2
    assert first_node.key == 1

    mid_node = default_dll.pop_left()
    assert len(default_dll) == 1
    assert mid_node.key == 22

    last_node = default_dll.pop_left()
    assert len(default_dll) == 0
    assert last_node.key == 333

    assert default_dll.pop_left() is None


def test_pop_right(default_dll):

    last_node = default_dll.pop_right()
    assert len(default_dll) == 2
    assert last_node.key == 333

    mid_node = default_dll.pop_right()
    assert len(default_dll) == 1
    assert mid_node.key == 22
    assert default_dll.first_node.key == 1
    assert default_dll.last_node.key == 1

    first_node = default_dll.pop_right()
    assert len(default_dll) == 0
    assert first_node.key == 1

    assert default_dll.pop_right() is None
    assert default_dll.first_node is None
    assert default_dll.last_node is None


def test_insert_at_front(default_dll):
    new_node = LinkedListNode(0)
    default_dll.insert(0, new_node)
    assert len(default_dll) == 4
    assert default_dll.first_node == new_node


def test_insert_inside(default_dll):
    new_node = LinkedListNode(55_555)
    default_dll.insert(1, new_node)
    assert len(default_dll) == 4
    assert default_dll.first_node.next == new_node


def test_insert_behind(default_dll):
    new_node = LinkedListNode(55_555)
    default_dll.insert(3, new_node)
    assert len(default_dll) == 4
    assert default_dll.last_node == new_node


def test_get_item(default_dll):
    assert default_dll[0].key == 1
    assert default_dll[1].key == 22
    assert default_dll[2].key == 333


def test_set_item(default_dll):

    default_dll[0] = LinkedListNode(999)
    assert default_dll[0].key == 999

    default_dll[1] = LinkedListNode(888)
    assert default_dll[1].key == 888

    default_dll[2] = LinkedListNode(777)
    assert default_dll[2].key == 777


def test_contains(default_dll):
    assert 1 in default_dll
    assert 22 in default_dll
    assert 333 in default_dll
    assert 4444 not in default_dll
