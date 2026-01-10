from typing import Optional, Union

from pycs.graph.edge import Edge
from pycs.graph.graph import Graph
from pycs.graph.vertex import Vertex


class AdjacencyMatrixGraph(Graph):

    def vertex_count(self) -> int:
        pass

    def edge_count(self) -> int:
        pass

    def vertices(self) -> list[Vertex]:
        pass

    def edges(self) -> list[Edge]:
        pass

    def get_edge(self, o: Vertex, d: Vertex) -> Edge | None:
        pass

    def degree(self, v: Vertex) -> int | None:
        pass

    def in_degree(self, v: Vertex) -> int | None:
        pass

    def out_degree(self, v: Vertex) -> int | None:
        pass

    def incident_edges(self, v: Vertex) -> list[Edge] | None:
        pass

    def insert_vertex(self, v: Vertex) -> None:
        pass

    def remove_vertex(self, v: Vertex) -> None:
        pass

    def insert_edge(
            self,
            o: Vertex,
            d: Vertex,
            x: Optional[int] = None
    ) -> None:
        pass

    def remove_edge(self, e: Edge) -> None:
        pass

    def __contains__(self, item: Union[Edge, Vertex]) -> bool:
        pass
