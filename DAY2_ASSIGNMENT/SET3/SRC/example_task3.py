from common import load_graph
from task3_graph import bfs_shortest_path, dfs_reachable
g = load_graph()
print(bfs_shortest_path(g, "PNQ", "CCU"))
print(dfs_reachable(g, "NAG"))
