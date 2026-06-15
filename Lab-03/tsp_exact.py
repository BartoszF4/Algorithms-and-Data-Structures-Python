def bfs_tsp(graph, start_city):
    num_cities = len(graph)
    queue = [(start_city, 0, [start_city])]
    min_distance = float('inf')
    min_path = []

    while queue:
        current_city, current_distance, path = queue.pop(0)

        if len(path) == num_cities:
            return_cost = graph[current_city][start_city]
            if return_cost != float('inf'):
                total_distance = current_distance + return_cost
                if total_distance < min_distance:
                    min_distance = total_distance
                    min_path = path + [start_city]
            continue

        for next_city in range(num_cities):
            if next_city not in path and graph[current_city][next_city] != float('inf'):
                queue.append((next_city, current_distance + graph[current_city][next_city], path + [next_city]))

    return min_path, min_distance

def dfs_tsp(graph, start_city):
    num_cities = len(graph)
    stack = [(start_city, 0, [start_city])]
    min_distance = float('inf')
    min_path = []

    while stack:
        current_city, current_distance, path = stack.pop()

        if len(path) == num_cities:
            return_cost = graph[current_city][start_city]
            if return_cost != float('inf'):
                total_distance = current_distance + return_cost
                if total_distance < min_distance:
                    min_distance = total_distance
                    min_path = path + [start_city]
            continue

        for next_city in range(num_cities):
            if next_city not in path and graph[current_city][next_city] != float('inf'):
                stack.append((next_city, current_distance + graph[current_city][next_city], path + [next_city]))

    return min_path, min_distance