from collections import defaultdict

# Неориентированный
def graph_from_edges(edges: list[list[int]]) -> dict[int, list[int]]:
    graph = defaultdict(list)
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    return graph

print(graph_from_edges([[1,2], [8,1], [3,2], [1,3]]))
