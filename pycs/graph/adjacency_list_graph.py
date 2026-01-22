from typing import Optional, TypeAlias

from pycs.graph.edge import Edge
from pycs.graph.graph import Graph
from pycs.graph.vertex import Vertex


EdgeList: TypeAlias = list[Edge]


class AdjacencyListGraph(Graph):

    def __init__(self):
        self._incidence_colls_map: dict[Vertex, EdgeList] = {}

    def vertex_count(self) -> int:
        return len(self._incidence_colls_map)

    def edge_count(self) -> int:
        return sum([
            len(ic) for _, ic in self._incidence_colls_map.items()
        ]) // 2

    def vertices(self) -> list[Vertex]:
        return list([v for v in self._incidence_colls_map])

    def edges(self) -> list[Edge]:
        return list({
            e for v, edges in self._incidence_colls_map.items() for e in edges
        })

    def get_edge(self, o: Vertex, d: Vertex) -> Edge | None:
        for e in self._incidence_colls_map[o]:
            if e.origin == o and e.destination == d:
                return e
        return None

    def degree(self, v: Vertex) -> int | None:
        if v in self._incidence_colls_map:
            return len([
                e for e in self._incidence_colls_map[v] if v in e.endpoints
            ])
        return None

    def in_degree(self, v: Vertex) -> int | None:
        if v in self._incidence_colls_map:
            return len([
                e for e in self._incidence_colls_map[v] if e.destination == v
            ])
        return None

    def out_degree(self, v: Vertex) -> int | None:
        if v in self._incidence_colls_map:
            return len([
                e for e in self._incidence_colls_map[v] if e.origin == v
            ])
        return None

    def incident_edges(self, v: Vertex) -> list[Edge] | None:
        if v in self._incidence_colls_map:
            return self._incidence_colls_map[v]
        return None

    def insert_vertex(self, v: Vertex) -> None:
        if v not in self._incidence_colls_map:
            self._incidence_colls_map[v] = []

    def remove_vertex(self, v: Vertex) -> None:
        if v in self._incidence_colls_map:
            self._incidence_colls_map.pop(v)
        for v in self._incidence_colls_map:
            self._incidence_colls_map[v] = [
                e
                for e in self._incidence_colls_map[v]
                if v not in e.endpoints
            ]

    def insert_edge(
            self,
            o: Vertex,
            d: Vertex,
            x: Optional[int] = None
    ) -> None:
        if o not in self._incidence_colls_map:
            raise ValueError(f"Trying to insert edge from vertex {o=}"
                             f"that is not present in the graph")
        if d not in self._incidence_colls_map:
            raise ValueError(f"Trying to insert edge to vertex {d=}"
                             f"that is not present in the graph")
        e: Edge = Edge(o, d, x)
        if e not in self._incidence_colls_map[o]:
            self._incidence_colls_map[o].append(e)
        if e not in self._incidence_colls_map[d]:
            self._incidence_colls_map[d].append(e)

    def remove_edge(self, e: Edge) -> None:
        if (o := e.origin) in self._incidence_colls_map:
            self._incidence_colls_map[o] = [
                oe
                for oe in self._incidence_colls_map[o]
                if e.endpoints != oe.endpoints
            ]
        if (d := e.destination) in self._incidence_colls_map:
            self._incidence_colls_map[d] = [
                de
                for de in self._incidence_colls_map[d]
                if e.endpoints != de.endpoints
            ]
