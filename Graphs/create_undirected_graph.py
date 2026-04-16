from collections import defaultdict

# Неориентированный
def graph_from_edges(edges: list[list[int]]) -> dict[int, list[int]]:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

print(graph_from_edges([[1,2], [8,1], [3,2], [1,3]]))
