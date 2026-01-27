from pytest import fixture

from pycs.data_structures.linked_list.linked_list_node import LinkedListNode
from pycs.data_structures.linked_list.singly_linked_list import (
    SinglyLinkedList)


@fixture
def default_sll() -> SinglyLinkedList:
    first, second, last = (
        LinkedListNode(1), LinkedListNode(22), LinkedListNode(333))
    sll = SinglyLinkedList()
    sll.append(first)
    sll.append(second)
    sll.append(last)
    return sll


def test_init():
    sll = SinglyLinkedList()
    assert len(sll) == 0
    first = LinkedListNode(key=22)
    sll.append(first)
    assert len(sll) == 1
    assert sll.first_node == first
    assert sll.last_node == first


def test_first_last_node():
    pass


def test_list_len():
    pass


def test_append():
    pass


def test_pop_left():
    pass


def test_pop_right():
    pass


def test_insert_remove():
    pass


def test_get_set_item():
    pass


def test_contains():
    pass
