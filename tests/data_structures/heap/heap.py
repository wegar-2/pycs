from pycs.data_structures.heap.heap import Heap

from pytest import fixture


def test_heap_construction():
    h = Heap()
    for x in [51, 7, 40, 20, 13]:
        h.append(x)
    assert len(h) == 7
    assert h.data == [7, 13, 40, 51, 20]


def test_heap_pop():
    pass


def test_raises_error_when_pop_empty_heap():
    pass


def test_heap_append():
    pass


def test_heap_peek_min():
    pass


def test_raises_error_when_peek_empty_heap():
    pass
