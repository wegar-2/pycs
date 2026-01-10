from pytest import fixture

from pycs.graph.edge import Edge
from pycs.graph.vertex import Vertex
from pycs.graph.adjacency_map_graph import AdjacencyMapGraph
from tests.graph.common import populate_empty_graph


@fixture
def graph():
    return populate_empty_graph(graph=AdjacencyMapGraph())


def test_insert_vertex(graph):
    v: Vertex = Vertex("H")
    graph.insert_vertex(v=v)
    assert v in graph.vertices()


def test_vertex_count():
    pass


def test_edge_count():
    pass


def test_vertices():
    pass


def test_edges():
    pass


def test_get_edge():
    pass


def test_degree():
    pass


def test_in_degree():
    pass


def test_out_degree():
    pass


def test_incident_edges():
    pass


def test_remove_vertex(graph):
    A, B = Vertex("A"), Vertex("B")
    e_AB: Edge = Edge(A, B)
    e_BA: Edge = Edge(B, A)
    graph.remove_vertex(v=B)
    assert B not in graph.vertices()
    assert not (e_AB in graph.edges())
    assert e_BA not in graph.edges()


def test_insert_edge():
    pass


def test_remove_edge():
    pass


def test_contains():
    pass
