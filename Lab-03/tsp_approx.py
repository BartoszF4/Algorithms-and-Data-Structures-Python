def greedy_tsp(graph, start_city):
    num_cities = len(graph)
    visited = [False] * num_cities
    visited[start_city] = True
    path = [start_city]
    current_city = start_city
    total_distance = 0

    for _ in range(num_cities - 1):
        next_city = -1
        min_edge = float('inf')
        for neighbor in range(num_cities):
            if not visited[neighbor] and graph[current_city][neighbor] < min_edge:
                min_edge = graph[current_city][neighbor]
                next_city = neighbor

        if next_city == -1:
            return [], float('inf')

        visited[next_city] = True
        path.append(next_city)
        total_distance += min_edge
        current_city = next_city

    return_cost = graph[current_city][start_city]
    if return_cost == float('inf'):
        return [], float('inf')

    path.append(start_city)
    total_distance += return_cost
    return path, total_distance


def mst_tsp(graph, start_city):
    num_cities = len(graph)
    in_mst = [False] * num_cities
    in_mst[start_city] = True
    mst_adj = [[] for _ in range(num_cities)]
    edges_used = 0

    while edges_used < num_cities - 1:
        min_edge = float('inf')
        u, v = -1, -1
        for i in range(num_cities):
            if in_mst[i]:
                for j in range(num_cities):
                    if not in_mst[j] and graph[i][j] < min_edge:
                        min_edge = graph[i][j]
                        u, v = i, j
        if v == -1:
            return [], float('inf')

        in_mst[v] = True
        mst_adj[u].append(v)
        mst_adj[v].append(u)
        edges_used += 1

    path = []
    stack = [start_city]
    visited = [False] * num_cities

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            path.append(current)
            for neighbor in reversed(mst_adj[current]):
                if not visited[neighbor]:
                    stack.append(neighbor)

    total_distance = 0
    for i in range(len(path) - 1):
        if graph[path[i]][path[i+1]] == float('inf'):
            return [], float('inf')
        total_distance += graph[path[i]][path[i+1]]

    return_cost = graph[path[-1]][start_city]
    if return_cost == float('inf'):
        return [], float('inf')

    path.append(start_city)
    total_distance += return_cost

    return path, total_distance