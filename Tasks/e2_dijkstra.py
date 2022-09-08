from typing import Hashable, Mapping, Union
import networkx as nx
from queue import PriorityQueue

def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    print(g, starting_node)

    cost = {}
    visited = {}
    # path = {}
    nodes = list(g.nodes)
    for node in nodes:
        cost[node] = float("inf")
        visited[node] = False
        # path[node] = []

    pq = PriorityQueue()
    cost[starting_node] = 0
    # path[starting_node] = [starting_node]
    pq.put((0, starting_node))

    while not pq.empty():
        current_node = pq.get()[1]
        if visited[current_node]:
            continue
        visited[current_node] = True

        for node in g.neighbors(current_node):
            weight = g.get_edge_data(current_node, node)['weight']
            if cost[current_node] + weight < cost[node]:
                cost[node] = cost[current_node] + weight
                # path[node] = path[current_node] + [node]
                pq.put((cost[node], node))

    return cost


if __name__ == "__main__":
    G = nx.DiGraph()
    G.add_nodes_from("ABCDEFG")
    G.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 3),
        ("C", "E", 4),
        ("E", "F", 3),
        ("B", "E", 8),
        ("C", "D", 1),
        ("D", "E", 2),
        ("B", "D", 2),
        ("G", "D", 1),
        ("D", "A", 2),
    ])
    print(dijkstra_algo(g=G, starting_node="A"))

