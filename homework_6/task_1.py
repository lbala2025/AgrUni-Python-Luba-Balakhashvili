def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    if start == end:
        return True

    visited.add(start)

    if start not in graph:
        return False

    for neighbor in graph[start]:
        if neighbor not in visited:
            if has_path(graph, neighbor, end, visited):
                return True

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E', 'K', 'M'],
    'E': [],
    'F': ['G', 'A'],
}

print(has_path(graph, 'A', 'E'))  # True  (A -> C -> E)
print(has_path(graph, 'C', 'D'))  # False
print(has_path(graph, 'A', 'D'))  # True  (A -> B -> D)
print(has_path(graph, 'E', 'A'))  # False
print(has_path(graph, 'F', 'K'))  # True (F -> A -> B -> D -> K)
