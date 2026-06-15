def bidirectional_search(graph, start_node, target_node):
    if start_node == target_node:
        return [start_node], 0.0

    num_nodes = len(graph)

    queue_start = [[0.0, [start_node]]]
    queue_target = [[0.0, [target_node]]]

    visited_start_cost = [float('inf')] * num_nodes
    visited_start_path = [[] for _ in range(num_nodes)]
    visited_start_cost[start_node] = 0.0
    visited_start_path[start_node] = [start_node]

    visited_target_cost = [float('inf')] * num_nodes
    visited_target_path = [[] for _ in range(num_nodes)]
    visited_target_cost[target_node] = 0.0
    visited_target_path[target_node] = [target_node]

    best_total_cost = float('inf')
    best_path = []

    while queue_start and queue_target:
        queue_start.sort(key=lambda x: x[0])
        queue_target.sort(key=lambda x: x[0])

        if queue_start[0][0] + queue_target[0][0] >= best_total_cost:
            break

        cost_start, path_start = queue_start.pop(0)
        current_start = path_start[-1]

        for neighbor in range(num_nodes):
            if graph[current_start][neighbor] != float('inf'):
                new_cost = cost_start + graph[current_start][neighbor]
                if new_cost < visited_start_cost[neighbor]:
                    new_path = path_start + [neighbor]
                    visited_start_cost[neighbor] = new_cost
                    visited_start_path[neighbor] = new_path
                    queue_start.append([new_cost, new_path])

                    if visited_target_cost[neighbor] != float('inf'):
                        total_cost = new_cost + visited_target_cost[neighbor]
                        if total_cost < best_total_cost:
                            best_total_cost = total_cost
                            best_path = new_path[:-1] + visited_target_path[neighbor][::-1]

        cost_target, path_target = queue_target.pop(0)
        current_target = path_target[-1]

        for neighbor in range(num_nodes):
            if graph[current_target][neighbor] != float('inf'):
                new_cost = cost_target + graph[current_target][neighbor]
                if new_cost < visited_target_cost[neighbor]:
                    new_path = path_target + [neighbor]
                    visited_target_cost[neighbor] = new_cost
                    visited_target_path[neighbor] = new_path
                    queue_target.append([new_cost, new_path])

                    if visited_start_cost[neighbor] != float('inf'):
                        total_cost = new_cost + visited_start_cost[neighbor]
                        if total_cost < best_total_cost:
                            best_total_cost = total_cost
                            best_path = visited_start_path[neighbor][:-1] + new_path[::-1]

    if best_total_cost == float('inf'):
        return [], float('inf')

    return best_path, best_total_cost