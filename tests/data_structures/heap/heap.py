from pytest import fixture, raises

from pycs.data_structures.heap.heap import Heap


@fixture
def default_heap() -> Heap:
    h = Heap()
    for x in [51, 7, 40, 20, 13]:
        h.append(x)
    return h


def test_heap_construction():
    h = Heap()
    for x in [51, 7, 40, 20, 13]:
        h.append(x)
    assert len(h) == 7
    assert h.data == [7, 13, 40, 51, 20]


def test_heap_pop(default_heap):
    assert [default_heap.pop() for _ in range(5)] == [7, 13, 20, 40, 51]


def test_raises_error_when_pop_empty_heap(default_heap):
    for _ in range(5):
        default_heap.pop()
    with raises(ValueError):
        default_heap.pop()


def test_heap_append():
    h = Heap()
    h.append(32)
    h.append(12)
    h.append(122)
    assert h.data == [12, 32, 122]


def test_heap_peek_min(default_heap):
    assert default_heap.peek_min() == 7


def test_raises_error_when_peek_empty_heap():
    h = Heap()
    with raises(ValueError):
        h.peek_min()
