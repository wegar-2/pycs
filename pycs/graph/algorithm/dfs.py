from pycs.graph.graph import Graph
from pycs.graph.vertex import Vertex
from pycs.graph.edge import Edge


def dfs(graph: Graph, sv: Vertex):

    if sv not in graph.vertices():
        raise ValueError(
            f"Received invalid starting vertex {sv} which is not a member "
            f"of the graph! "
        )

    next_vertices: list[Vertex] = [sv]
    vertices_levels: dict[Vertex, int] = {sv: 0}

    while next_vertices:
        pass

    return None
