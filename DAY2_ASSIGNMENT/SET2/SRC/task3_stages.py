from collections import deque

def bfs_shortest_path(graph, start, goal):
    """Fewest stages. Returns (path or None, steps)."""
    if start == goal:
        return [start], 0
    parent, q = {start: None}, deque([start])
    while q:
        u = q.popleft()
        for v in graph.get(u, []):
            if v not in parent:
                parent[v] = u
                if v == goal:
                    path = [v]
                    while parent[path[-1]] is not None:
                        path.append(parent[path[-1]])
                    return path[::-1], len(path) - 1
                q.append(v)
    return None, -1

def find_cycle(graph):
    """DFS with 3 colours. WHITE = new, GREY = on current path, BLACK = done.
    An edge into a GREY stage closes a loop. Returns the loop or None."""
    WHITE, GREY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}
    for s in graph:
        if color[s] != WHITE:
            continue
        color[s] = GREY
        path, stack = [s], [(s, iter(graph[s]))]
        while stack:
            u, it = stack[-1]
            for v in it:
                state = color.get(v, WHITE)
                if state == GREY:
                    return path[path.index(v):] + [v]
                if state == WHITE:
                    color[v] = GREY
                    path.append(v)
                    stack.append((v, iter(graph.get(v, []))))
                    break
            else:
                color[u] = BLACK
                stack.pop(); path.pop()
    return None
