from typing import Optional

from pycs.graph.edge import Edge
from pycs.graph.graph import Graph
from pycs.graph.vertex import Vertex


class EdgeListGraph(Graph):

    def __init__(self):
        """
        Although the class is called EdgeList, the vertices and edges are
        stored in sets. This is necessary in order to ensure O(1) complexity
        of insertions.
        """
        self._vertices: set[Vertex] = set()
        self._edges: set[Edge] = set()

    def vertex_count(self) -> int:
        return len(self._vertices)

    def edge_count(self) -> int:
        return len(self._edges)

    def vertices(self) -> list[Vertex]:
        return list(self._vertices)

    def edges(self) -> list[Edge]:
        return list(self._edges)

    def get_edge(self, o: Vertex, d: Vertex) -> Edge | None:
        for e in self._edges:
            if e.origin == o and e.destination == d:
                return e
        return None

    def degree(self, v: Vertex) -> int | None:
        if v in self._vertices:
            n = 0
            for e in self._edges:
                if v in e.endpoints:
                    n += 1
            return n
        return None

    def in_degree(self, v: Vertex) -> int | None:
        if v in self._vertices:
            n = 0
            for e in self._edges:
                if v == e.destination:
                    n += 1
            return n
        return None

    def out_degree(self, v: Vertex) -> int | None:
        if v in self._vertices:
            n = 0
            for e in self._edges:
                if v == e.origin:
                    n += 1
            return n
        return None

    def incident_edges(self, v: Vertex) -> list[Edge] | None:
        if v in self._vertices:
            return [e for e in self._edges if v in e.endpoints]
        return None

    def insert_vertex(self, v: Vertex) -> None:
        self._vertices.add(v)

    def remove_vertex(self, v: Vertex) -> None:
        self._vertices.remove(v)
        self._edges = {e for e in self._edges if v not in e.endpoints}

    def insert_edge(
            self,
            o: Vertex,
            d: Vertex,
            x: Optional[int] = None
    ) -> None:
        if o not in self._vertices:
            raise ValueError(f"Trying to insert edge from vertex {o=}"
                             f"that is not present in the graph")
        if d not in self._vertices:
            raise ValueError(f"Trying to insert edge to vertex {d=}"
                             f"that is not present in the graph")
        self._edges.add(Edge(o, d, x))

    def remove_edge(self, e: Edge) -> None:
        self._edges.remove(e)
