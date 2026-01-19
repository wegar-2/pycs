from pycs.graph.graph import Graph
from pycs.graph.vertex import Vertex
from pycs.graph.algorithm.common import BFSResult

__all__ = ["bfs"]


def bfs(graph: Graph, sv: Vertex) -> BFSResult:
    if sv not in graph.vertices():
        raise ValueError(
            f"Received invalid starting vertex {sv} which is not a member "
            f"of the graph! "
        )

    levels_map: dict[Vertex, int] = {sv: 0}
    parent_vertex_map: dict[Vertex, Vertex | None] = {sv: None}
    frontier: list[Vertex] = [sv]
    i = 1

    while frontier:
        next_vertices: list[Vertex] = []
        for fv in frontier:
            if oes := graph.outgoing_incident_edges(v=fv) is not None:
                fv_next: list[Vertex] = [e.destination for e in oes]
                for u in fv_next:
                    if u not in levels_map:
                        levels_map[u] = i
                        parent_vertex_map[u] = fv
                        next_vertices.append(u)
        i += 1
        frontier = next_vertices

    return {
        "parent_vertex_map": parent_vertex_map,
        "levels_map": levels_map
    }
