from abc import ABC, abstractmethod
from typing import Any, Optional, Union

from pycs.graph.edge import Edge
from pycs.graph.vertex import Vertex
from pycs.graph.exception import InvalidContainsException


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
    def get_edge(self, o: Vertex, d: Vertex) -> Edge | None:
        pass

    @abstractmethod
    def degree(self, v: Vertex) -> int | None:
        pass

    @abstractmethod
    def in_degree(self, v: Vertex) -> int | None:
        pass

    @abstractmethod
    def out_degree(self, v: Vertex) -> int | None:
        pass

    @abstractmethod
    def incident_edges(self, v: Vertex) -> list[Edge] | None:
        pass

    def outgoing_incident_edges(self, v: Vertex) -> list[Edge] | None:
        ies = self.incident_edges(v)
        if ies is not None:
            return [e for e in ies if e.origin == v]
        return None

    def incoming_incident_edges(self, v: Vertex) -> list[Edge] | None:
        ies = self.incident_edges(v)
        if ies is not None:
            return [e for e in ies if e.destination == v]
        return None

    @abstractmethod
    def insert_vertex(self, v: Vertex) -> None:
        pass

    @abstractmethod
    def remove_vertex(self, v: Vertex) -> None:
        pass

    @abstractmethod
    def insert_edge(
            self,
            o: Vertex,
            d: Vertex,
            x: Optional[Any] = None
    ) -> None:
        pass

    @abstractmethod
    def remove_edge(self, e: Edge) -> None:
        pass

    def __contains__(self, item: Union[Edge, Vertex]) -> bool:
        if isinstance(item, Edge):
            return item in self.edges()
        elif isinstance(item, Vertex):
            return item in self.vertices()
        else:
            raise InvalidContainsException(item)
