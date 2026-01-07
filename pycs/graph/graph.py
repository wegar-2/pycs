from abc import ABC, abstractmethod
from typing import Any

from pycs.graph.edge import Edge
from pycs.graph.vertex import Vertex


class Graph(ABC):

    @abstractmethod
    def vertex_count(self) -> int:
        pass

    @abstractmethod
    def edge_count(self) -> int:
        pass

    @abstractmethod
    def vertices(self) -> list[Vertex]:
        pass

    @abstractmethod
    def edges(self) -> list[Edge]:
        pass

    @abstractmethod
    def get_edge(self, u: Vertex, v: Vertex) -> Edge | None:
        pass

    @abstractmethod
    def degree(self, v: Vertex) -> int:
        pass

    @abstractmethod
    def in_degree(self, v: Vertex) -> int:
        pass

    @abstractmethod
    def out_degree(self, v: Vertex) -> int:
        pass

    @abstractmethod
    def incident_edges(self, v: Vertex) -> list[Edge]:
        pass

    @abstractmethod
    def insert_vertex(self, v: Vertex) -> None:
        pass

    @abstractmethod
    def remove_vertex(self, v: Vertex) -> None:
        pass

    @abstractmethod
    def insert_edge(self, o: Vertex, d: Vertex, x: Any) -> None:
        pass

    @abstractmethod
    def remove_edge(self, e: Edge) -> None:
        pass
