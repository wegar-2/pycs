from typing import Any, TypeAlias

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
        return sum([len(ic) for _, ic in self._incidence_colls_map.items()])

    def vertices(self) -> list[Vertex]:
        return list([v for v in self._incidence_colls_map])

    def edges(self) -> list[Edge]:
        return list({
            e for v, edges in self._incidence_colls_map.items() for e in edges
        })

    def get_edge(self, o: Vertex, d: Vertex) -> Edge | None:

        orig: bool = False
        if o in self._incidence_colls_map:
            orig = any([])

        dest: bool = False


        if orig and dest:
            for e in self._incidence_colls_map[o]:
                if e.origin == o and e.destination == d:
                    return e
        return None

    def degree(self, v: Vertex) -> int:
        pass

    def in_degree(self, v: Vertex) -> int:
        pass

    def out_degree(self, v: Vertex) -> int:
        if v in self._incidence_colls_map:
            return len([
                e for e in self._incidence_colls_map[v] if e.origin == v
            ])
        return 0

    def incident_edges(self, v: Vertex) -> list[Edge] | None:
        if v in self._incidence_colls_map:
            return self._incidence_colls_map[v]
        return None

    def insert_vertex(self, v: Vertex) -> None:
        if v not in self._incidence_colls_map:
            self._incidence_colls_map[v] = []

    def remove_vertex(self, v: Vertex) -> None:
        pass

    def insert_edge(self, o: Vertex, d: Vertex, x: Any) -> None:
        pass

    def remove_edge(self, e: Edge) -> None:
        pass
