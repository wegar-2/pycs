from pycs.graph.edge import Edge
from pycs.graph.graph import Graph
from pycs.graph.vertex import Vertex


class EdgeListGraph(Graph):

    def __init__(self):
        self._vertices: list[Vertex] = []
        self._edges: list[Edge] = []

    def vertex_count(self) -> int:
        return len(self._vertices)

    def edge_count(self) -> int:
        return len(self._edges)

    def vertices(self) -> list[Vertex]:
        return self._vertices

    def edges(self) -> list[Edge]:
        return self._edges

    def get_edge(self, o: Vertex, d: Vertex) -> Edge | None:
        pass

    def degree(self, v: Vertex) -> int:
        pass

    def in_degree(self, v: Vertex) -> int:
        pass

    def out_degree(self, v: Vertex) -> int:
        pass

    def incident_edges(self, v: Vertex) -> list[Edge]:
        pass

    def insert_vertex(self, v: Vertex) -> None:
        pass

    def remove_vertex(self, v: Vertex) -> None:
        pass

    def insert_edge(self, o: Vertex, d: Vertex, x: Any) -> None:
        pass

    def remove_edge(self, e: Edge) -> None:
        pass
