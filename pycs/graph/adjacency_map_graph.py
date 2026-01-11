from typing import Optional, TypeAlias

from pycs.graph.edge import Edge
from pycs.graph.graph import Graph
from pycs.graph.vertex import Vertex

IncidenceMap: TypeAlias = dict[Vertex, Edge]


class AdjacencyMapGraph(Graph):
    """
    directed graph!
    """

    def __init__(self):
        self._outgoing: dict[Vertex, IncidenceMap] = {}
        self._incoming: dict[Vertex, IncidenceMap] = {}

    def insert_vertex(self, v: Vertex) -> None:
        if v not in self._outgoing:
            self._outgoing[v] = {}
        if v not in self._incoming:
            self._incoming[v] = {}

    def insert_edge(
            self,
            o: Vertex,
            d: Vertex,
            x: Optional[int] = None
    ) -> None:
        if o not in self._outgoing:
            raise ValueError(f"Trying to insert edge from vertex {o=}"
                             f"that is not present in the graph")
        if d not in self._incoming:
            raise ValueError(f"Trying to insert edge to vertex {d=}"
                             f"that is not present in the graph")
        e: Edge = Edge(o, d, x)
        self._outgoing[o][d] = e
        self._incoming[d][o] = e

    def vertex_count(self) -> int:
        return len(self._outgoing)

    def edge_count(self) -> int:
        return sum([len(self._outgoing[v]) for v in self._outgoing])

    def edges(self) -> list[Edge]:
        return [
            self._outgoing[o][d]
            for o in self._outgoing
            for d in self._outgoing[o]
        ]

    def vertices(self) -> list[Vertex]:
        vertices: set[Vertex] = set()
        for v in self._outgoing:
            vertices.add(v)
        for v in self._incoming:
            vertices.add(v)
        return [v for v in vertices]

    def get_edge(self, u: Vertex, d: Vertex) -> Edge | None:
        if u in self._outgoing:
            if d in self._outgoing[u]:
                return self._outgoing[u][d]
            return None
        return None

    def remove_edge(self, e: Edge) -> None:
        if (o := e.origin) in self._outgoing:
            if (d := e.destination) in self._outgoing[o]:
                self._outgoing[o].pop(d)
        if (d := e.destination) in self._incoming:
            if (o := e.origin) in self._incoming[d]:
                self._outgoing[d].pop(o)

    def remove_vertex(self, v: Vertex) -> None:
        if v in self._outgoing:
            self._outgoing.pop(v)
        if v in self._incoming:
            self._incoming.pop(v)

        for u in self._outgoing:
            self._outgoing[u] = {
                d: e
                for d, e in self._outgoing[u].items()
                if v not in e.endpoints
            }
        for u in self._incoming:
            self._incoming[u] = {
                d: e
                for d, e in self._outgoing[u].items()
                if v not in e.endpoints
            }


    def in_degree(self, v: Vertex) -> int | None:
        if v in self._incoming:
            return len(self._incoming[v])
        return None

    def out_degree(self, v: Vertex) -> int | None:
        if v in self._outgoing:
            return len(self._outgoing[v])
        return None

    def degree(self, v: Vertex) -> int | None:
        in_deg = self.in_degree(v)
        out_deg = self.out_degree(v)
        if in_deg is None and out_deg is None:
            return None
        else:
            return (
                    (in_deg if in_deg is not None else 0) +
                    (out_deg if out_deg is not None else 0)
            )

    def incident_edges(self, v: Vertex) -> list[Edge] | None:
        if v in self._outgoing or v in self._incoming:
            return [
                self._outgoing[v][k] for k in self._outgoing[v]
            ] + [
                self._incoming[v][k] for k in self._incoming[v]
            ]
        return None
