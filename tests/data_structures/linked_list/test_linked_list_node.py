from pycs.data_structures.linked_list.linked_list_node import LinkedListNode


def test_init():
    node = LinkedListNode(1)
    assert isinstance(node, LinkedListNode)


def test_key_and_value():
    node = LinkedListNode(1, value={"a": 123})
    assert node.key == 1
    assert node.value == {"a": 123}
    node.value = "qwerty"
    assert node.value == "qwerty"


def test_prev_next():
    first = LinkedListNode(key=1)
    second = LinkedListNode(key=2)
    last = LinkedListNode(key=3)
    first.next = second
    second.next = last
    second.prev = first
    last.prev = second

    assert first.next == second
    assert second.next == last
    assert last.prev == second
    assert second.prev == first
