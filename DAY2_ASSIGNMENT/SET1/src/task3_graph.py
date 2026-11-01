"""Task 3 - Microservice deployment order (graph), with BFS and DFS, plus cycle detection.

The graph is stored as {service: [services it DEPENDS ON]}, like the arrows in the brief
(cart -> pricing -> inventory). A service can only be deployed after everything it depends on.
"""
from collections import deque
from common import load_dependencies


def all_services(depends_on):
    """Every service name once, in the order first seen."""
    seen = []
    for service, deps in depends_on.items():
        for name in [service] + deps:
            if name not in seen:
                seen.append(name)
    return seen


def deploy_order_dfs(depends_on):
    """Depth-first search. Returns (order, cycle). One of them is None."""
    WHITE, GREY, BLACK = 0, 1, 2          # not visited / on the current path / finished
    state = {s: WHITE for s in all_services(depends_on)}
    order, path = [], []

    def visit(service):
        state[service] = GREY
        path.append(service)
        for dep in depends_on.get(service, []):
            if state[dep] == GREY:                      # we came back to the current path
                return path[path.index(dep):] + [dep]   # -> circular dependency
            if state[dep] == WHITE:
                cycle = visit(dep)
                if cycle:
                    return cycle
        path.pop()
        state[service] = BLACK
        order.append(service)                           # all dependencies are already in order
        return None

    for service in list(state):
        if state[service] == WHITE:
            cycle = visit(service)
            if cycle:
                return None, cycle
    return order, None


def deploy_order_bfs(depends_on, steps=None):
    """Breadth-first search (Kahn's method). Returns (order, stuck_services)."""
    services = all_services(depends_on)
    waiting = {s: len(depends_on.get(s, [])) for s in services}     # dependencies not yet deployed
    dependents = {s: [] for s in services}
    for service, deps in depends_on.items():
        for dep in deps:
            dependents[dep].append(service)

    queue = deque(s for s in services if waiting[s] == 0)
    order = []
    while queue:
        service = queue.popleft()
        order.append(service)
        ready = []
        for other in dependents[service]:
            waiting[other] -= 1
            if waiting[other] == 0:
                queue.append(other)
                ready.append(other)
        if steps is not None:
            steps.append((service, ready, list(queue)))
    if len(order) < len(services):
        return None, [s for s in services if s not in order]       # these can never be deployed
    return order, None


def is_valid_order(order, depends_on):
    """Check: every service appears after all the services it depends on."""
    position = {s: i for i, s in enumerate(order)}
    return all(position[d] < position[s] for s, deps in depends_on.items() for d in deps)


def main():
    deps = load_dependencies()
    print("Dependencies (service -> depends on):")
    for s, d in deps.items():
        print(f"  {s:<13} -> {', '.join(d) if d else '(nothing)'}")

    order_dfs, _ = deploy_order_dfs(deps)
    order_bfs, _ = deploy_order_bfs(deps)
    print("\nA) Valid deployment order")
    print("  DFS:", " , ".join(order_dfs), "| valid:", is_valid_order(order_dfs, deps))
    print("  BFS:", " , ".join(order_bfs), "| valid:", is_valid_order(order_bfs, deps))

    cyclic = {k: list(v) for k, v in deps.items()}
    cyclic["inventory"].append("cart")          # now cart -> pricing -> inventory -> cart
    print("\nB) Circular dependency: add 'inventory depends on cart'")
    order, cycle = deploy_order_dfs(cyclic)
    print("  DFS found the loop :", " -> ".join(cycle))
    order, stuck = deploy_order_bfs(cyclic)
    print("  BFS cannot deploy  :", ", ".join(stuck), "(they wait for each other forever)")
    return {"services": len(all_services(deps)), "edges": sum(len(v) for v in deps.values()),
            "cycle": cycle, "stuck": stuck}


if __name__ == "__main__":
    main()
