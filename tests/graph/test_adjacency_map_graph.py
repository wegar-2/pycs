from pytest import fixture

from pycs.graph.adjacency_map_graph import AdjacencyMapGraph
from tests.graph.common import populate_empty_graph


@fixture
def graph():
    return populate_empty_graph(graph=AdjacencyMapGraph())


def test_insert_vertex():
    pass


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


def test_insert_vertex():
    pass


def test_remove_vertex():
    pass


def test_insert_edge():
    pass


def test_remove_edge():
    pass


def test_contains():
    pass