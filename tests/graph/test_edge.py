from pycs.graph.edge import Edge
from pycs.graph.vertex import Vertex

from pytest import fixture


@fixture
def edge() -> Edge:
    return Edge(Vertex("A"), Vertex("B"), element=123)


@fixture
def o() -> Vertex:
    return Vertex("A")


@fixture
def d() -> Vertex:
    return Vertex("B")


def test_init(edge):
    assert isinstance(edge, Edge)


def test_endpoints(edge, o, d):
    assert edge.endpoints == (o, d)


def test_origin(edge, o):
    assert edge.origin == o


def test_destination(edge, d):
    assert edge.destination == d


def test_opposite(edge, o, d):
    assert edge.opposite(o) == d
    assert edge.opposite(d) == o


def test_element(edge):
    assert edge.element == 123


def test_eq(edge):
    assert edge == Edge(Vertex("A"), Vertex("B"), 123)
