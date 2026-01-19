from pytest import fixture


from pycs.graph.vertex import Vertex
from pycs.graph.edge import Edge
from pycs.graph.graph import Graph
from pycs.graph.adjacency_map_graph import AdjacencyMapGraph
from pycs.graph.algorithm.dfs import dfs


@fixture
def digraph() -> Graph:
    graph = AdjacencyMapGraph()

    graph.insert_vertex(Vertex("A"))
    graph.insert_vertex(Vertex("A"))
    graph.insert_vertex(Vertex("A"))
    graph.insert_vertex(Vertex("A"))



def test_dfs():
    pass
