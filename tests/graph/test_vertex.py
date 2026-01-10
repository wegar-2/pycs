from pycs.graph.vertex import Vertex


def test_init():
    v = Vertex("A")
    assert isinstance(v, Vertex)


def test_element():
    v = Vertex("A")
    u = Vertex("B")
    assert v.element == "A"
    assert u.element == "B"


def test_hash():
    v = Vertex("A")
    u = Vertex("A")
    assert hash(v) == hash(u)


def test_eq():
    v = Vertex("A")
    u = Vertex("A")
    assert v == u
