# Время выполнения: O(n+m)
# Память: O(n)

from collections import deque

def shortest_path(graph: dict[int, list[int]], start: int, end: int) -> int:
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        node, dist = queue.popleft()

        if node == end:
            return dist
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, dist + 1))
                visited.add(neighbor)
    return -1

print(shortest_path({1: [2],2: [1, 3],3: [2, 5, 4],4: [3, 7],5: [3, 7],7: [4, 5]}, 5, 1))
