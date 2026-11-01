from common import load_stage_graph
from task3_stages import bfs_shortest_path, find_cycle
g = load_stage_graph()
print(bfs_shortest_path(g, "REGISTRATION", "SETTLEMENT"))
print(find_cycle(g))
