from pycs.graph.edge import Edge
from pycs.graph.graph import Graph
from pycs.graph.vertex import Vertex

__all__ = [
    "populate_empty_graph",
    "make_vertices",
    "make_edges"
]


def make_vertices() -> list[Vertex]:
    return [
        Vertex(element=letter)
        for letter in
        ["A", "B", "C", "D", "E", "F", "G"]
    ]


def make_edges() -> list[Edge]:
    vertices: list[Vertex] = make_vertices()
    A, B, C, D, E, F, G = vertices
    return [
        Edge(A, B),
        Edge(B, A),
        Edge(A, D),
        Edge(C, A),
        Edge(E, F)
    ]


def populate_empty_graph(graph: Graph) -> Graph:
    vertices: list[Vertex] = make_vertices()
    for v in vertices:
        graph.insert_vertex(v)
    edges: list[Edge] = make_edges()
    for e in edges:
        graph.insert_edge(o=e.origin, d=e.destination, x=e.element)
    return graph


if __name__ == "__main__":
    from pycs.graph.adjacency_map_graph import AdjacencyMapGraph
    amg = populate_empty_graph(graph=AdjacencyMapGraph())
