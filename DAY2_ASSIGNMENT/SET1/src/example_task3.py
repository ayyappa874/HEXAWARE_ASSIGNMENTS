# Example 3 - deployment order for a small set of services
from task3_graph import deploy_order_dfs, deploy_order_bfs

depends_on = {"cart": ["pricing"], "pricing": ["inventory"], "inventory": []}   # cart -> pricing -> inventory

print("DFS order:", deploy_order_dfs(depends_on)[0])
print("BFS order:", deploy_order_bfs(depends_on)[0])

depends_on["inventory"] = ["cart"]                     # now they depend on each other in a circle
order, cycle = deploy_order_dfs(depends_on)
print("With a circle -> order:", order, "| cycle found:", cycle)
