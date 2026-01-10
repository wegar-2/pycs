from pytest import fixture, raises

from pycs.graph.edge import Edge
from pycs.graph.vertex import Vertex
from pycs.graph.adjacency_map_graph import AdjacencyMapGraph
from tests.graph.common import populate_empty_graph, make_edges, make_vertices


@fixture
def graph():
    return populate_empty_graph(graph=AdjacencyMapGraph())


def test_insert_vertex(graph):
    v: Vertex = Vertex("H")
    graph.insert_vertex(v=v)
    assert v in graph.vertices()


def test_vertex_count(graph):
    assert graph.vertex_count() == 7


def test_edge_count(graph):
    assert graph.edge_count() == 5


def test_vertices(graph):
    assert set(graph.vertices()) == set(make_vertices())


def test_edges(graph):
    assert set(graph.edges()) == set(make_edges())


def test_get_edge(graph):
    assert (graph.get_edge(Vertex("A"), Vertex("B")) ==
            Edge(Vertex("A"), Vertex("B")))
    assert graph.get_edge(Vertex("A"), Vertex("K")) is None


def test_degree(graph):
    assert graph.degree(Vertex("A")) == 4
    assert graph.degree(Vertex("B")) == 2
    assert graph.degree(Vertex("C")) == 1
    assert graph.degree(Vertex("G")) == 0


def test_in_degree(graph):
    assert graph.in_degree(Vertex("A")) == 2
    assert graph.in_degree(Vertex("B")) == 1
    assert graph.in_degree(Vertex("C")) == 0
    assert graph.in_degree(Vertex("G")) == 0


def test_out_degree(graph):
    assert graph.out_degree(Vertex("A")) == 2
    assert graph.out_degree(Vertex("B")) == 1
    assert graph.out_degree(Vertex("C")) == 1
    assert graph.out_degree(Vertex("G")) == 0


def test_incident_edges(graph):
    # assert (
    #     set(graph.incident_edges(v=Vertex("A"))) == set([
    #         Edge(Vertex("A"), Vertex("B")),
    #         Edge(Vertex("B"), Vertex("A"))
    #     ])
    # )
    pass

def test_remove_vertex(graph):
    A, B = Vertex("A"), Vertex("B")
    e_AB: Edge = Edge(A, B)
    e_BA: Edge = Edge(B, A)
    graph.remove_vertex(v=B)
    assert B not in graph.vertices()
    assert not (e_AB in graph.edges())
    assert e_BA not in graph.edges()


def test_insert_valid_edge(graph):
    e0 = Edge(Vertex("A"), Vertex("B"))
    e1 = Edge(Vertex("A"), Vertex("G"))
    graph.insert_edge(Vertex("A"), Vertex("B"))
    graph.insert_edge(Vertex("A"), Vertex("G"))
    assert e0 in graph
    assert e1 in graph


def test_insert_invalid_edge(graph):
    with raises(ValueError):
        graph.insert_edge(Vertex("X"), Vertex("Y"))
    with raises(ValueError):
        graph.insert_edge(Vertex("A"), Vertex("Z"))


def test_remove_edge(graph):
    e: Edge = Edge(Vertex("A"), Vertex("B"))
    graph.remove_edge(e)
    assert e not in graph.edges()


def test_contains(graph):
    assert Vertex("A") in graph
    assert Vertex("X") not in graph
    assert Edge(Vertex("A"), Vertex("B")) in graph
    assert Edge(Vertex("A"), Vertex("G")) not in graph
