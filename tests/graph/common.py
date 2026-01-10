from pycs.graph.edge import Edge
from pycs.graph.graph import Graph
from pycs.graph.vertex import Vertex


def populate_empty_graph(graph: Graph) -> Graph:

    vertices: list[Vertex] = [
        Vertex(element=letter) for letter in ["A", "B", "C", "D", "E", "F", "G"]
    ]
    A, B, C, D, E, F, G = vertices # noqa
    for v in vertices:
        graph.insert_vertex(v)

    edges: list[Edge] = [
        Edge(A, B),
        Edge(A, C),
        Edge(A, D)
    ]
    for e in edges:
        graph.insert_edge(o=e.origin, d=e.destination, x=e.element)

    return graph
