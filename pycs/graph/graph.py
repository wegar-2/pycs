from abc import ABC, abstractmethod


class Graph(ABC):

    @abstractmethod
    def vertex_count(self) -> int:
        pass

    @abstractmethod
    def edge_count(self) -> int:
        pass

    @abstractmethod
    def vertices(self) -> list:
        pass

    @abstractmethod
    def edges(self) -> list:
        pass

    