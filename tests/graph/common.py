from pycs.graph.edge import Edge
from pycs.graph.graph import Graph
from pycs.graph.vertex import Vertex

__all__ = [
    "populate_empty_graph",
    "populate_graph_for_search",
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


def populate_graph_for_search(graph: Graph) -> Graph:
    vertices: list[Vertex] = make_vertices()
    A, B, C, D, E, F, G = vertices
    for v in vertices:
        graph.insert_vertex(v)

    graph.insert_edge(A, B)
    graph.insert_edge(B, C)
    graph.insert_edge(C, D)
    graph.insert_edge(D, E)
    graph.insert_edge(D, F)
    graph.insert_edge(E, G)

    return graph


if __name__ == "__main__":
    from pycs.graph.adjacency_map_graph import AdjacencyMapGraph
    from pycs.graph.adjacency_list_graph import AdjacencyListGraph
    alg = populate_empty_graph(graph=AdjacencyListGraph())
    e = alg.get_edge(Vertex("A"), Vertex("B"))
    print("halt")
