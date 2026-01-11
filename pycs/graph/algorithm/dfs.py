from typing import Optional

from pycs.graph.graph import Graph
from pycs.graph.vertex import Vertex


def dfs(
        graph: Graph,
        sv: Vertex,
        visited: Optional[list[Vertex]] = None,
        parent_vertex_map: Optional[dict[Vertex, Vertex]] = None
):
    if visited is None:
        visited: list[Vertex] = [sv]
    if parent_vertex_map is None:
        parent_vertex_map: dict[Vertex, Vertex | None] = {sv: None}

    if sv not in graph.vertices():
        raise ValueError(
            f"Received invalid starting vertex {sv} which is not a member "
            f"of the graph! "
        )

    next_vertices: list[Vertex] = [
        e.destination for e in graph.outgoing_incident_edges(sv)
    ]

    for nv in next_vertices:
        if nv not in visited:
            visited.append(nv)
            parent_vertex_map[nv] = sv
            res = dfs(
                graph=graph,
                sv=nv,
                visited=visited,
                parent_vertex_map=parent_vertex_map
            )
            parent_vertex_map = res["parent_vertex_map"]
            visited = res["visited"]

    return {
        "parent_vertex_map": parent_vertex_map,
        "visited": visited
    }


if __name__ == "__main__":
    from pycs.graph.adjacency_map_graph import AdjacencyMapGraph
    from tests.graph.common import populate_graph_for_search

    graph = populate_graph_for_search(graph=AdjacencyMapGraph())

    res = dfs(graph=graph, sv=Vertex("A"))

    print("Halt! ")
