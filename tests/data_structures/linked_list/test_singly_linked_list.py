from pytest import fixture, raises

from pycs.data_structures.linked_list.linked_list_node import LinkedListNode
from pycs.data_structures.linked_list.singly_linked_list import (
    SinglyLinkedList)


def make_default_sll() -> SinglyLinkedList:
    first, second, last = (
        LinkedListNode(1), LinkedListNode(22), LinkedListNode(333))
    sll = SinglyLinkedList()
    sll.append(first)
    sll.append(second)
    sll.append(last)
    return sll


def test_first_last_node_and_len():

    sll = SinglyLinkedList()
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


def test_append():
    default_sll = make_default_sll()
    new_node = LinkedListNode(4444)
    default_sll.append(new_node)
    assert len(default_sll) == 4
    assert default_sll.last_node == new_node


def test_pop_left():

    default_sll = make_default_sll()

    first_node = default_sll.pop_left()
    assert len(default_sll) == 2
    assert first_node.key == 1

    mid_node = default_sll.pop_left()
    assert len(default_sll) == 1
    assert mid_node.key == 22

    last_node = default_sll.pop_left()
    assert len(default_sll) == 0
    assert last_node.key == 333

    assert default_sll.pop_left() is None


def test_pop_right():

    default_sll = make_default_sll()

    last_node = default_sll.pop_right()
    assert len(default_sll) == 2
    assert last_node.key == 333

    mid_node = default_sll.pop_right()
    assert len(default_sll) == 1
    assert mid_node.key == 22
    assert default_sll.first_node.key == 1
    assert default_sll.last_node.key == 1

    first_node = default_sll.pop_right()
    assert len(default_sll) == 0
    assert first_node.key == 1

    assert default_sll.pop_right() is None
    assert default_sll.first_node is None
    assert default_sll.last_node is None


def test_insert():
    pass


def test_get_set_item():
    pass


def test_contains():
    pass
