from typing import TypedDict

from pycs.graph.vertex import Vertex


__all__ = [
    "BFSResult",
    "DFSResult",
    "vertex_path"
]


BFSResult = TypedDict("BFSResult", {
    "parent_vertex_map": dict[Vertex, Vertex],
    "levels_map": dict[Vertex, int]
})


DFSResult = TypedDict("DFSResult", {
    "parent_vertex_map": dict[Vertex, Vertex],
    "visited": list[Vertex]
})


def vertex_path(
        parent_vertex_map: dict[Vertex, Vertex],
        sv: Vertex,
        ev: Vertex
) -> list[Vertex]:
    pass
