from collections import deque

def bfs_shortest_path(graph, start, goal):
    """Fewest hops. Returns (path list or None, hops)."""
    if start == goal:
        return [start], 0
    parent, seen, q = {start: None}, {start}, deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in seen:
                seen.add(v); parent[v] = u
                if v == goal:
                    path = [v]
                    while parent[path[-1]] is not None:
                        path.append(parent[path[-1]])
                    path.reverse()
                    return path, len(path) - 1
                q.append(v)
    return None, -1

def dfs_reachable(graph, start):
    """All hubs reachable from start, in DFS visit order (iterative)."""
    seen, order, stack = set(), [], [start]
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u); order.append(u)
        for v in reversed(graph[u]):
            if v not in seen:
                stack.append(v)
    return order
