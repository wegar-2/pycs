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

    v_path: list[Vertex] = [ev]

    if ev not in parent_vertex_map:
        raise ValueError(
            f"End vertex {ev} not in the keys of the parent_vertex_map! ")

    next_v: Vertex = ev

    while next_v != sv:
        next_v = parent_vertex_map[next_v]
        v_path.append(next_v)

    return v_path[::-1]
