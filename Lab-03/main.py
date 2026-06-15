from graph import generate_cities, create_graph
from tsp_exact import bfs_tsp, dfs_tsp
from tsp_approx import greedy_tsp, mst_tsp
from bidirectional import bidirectional_search


def print_matrix(matrix):
    for row in matrix:
        formatted_row = []
        for val in row:
            if val == float('inf'):
                formatted_row.append(f"{'inf':>7}")
            else:
                formatted_row.append(f"{val:>7.2f}")
        print(" ".join(formatted_row))
    print()


def main():
    num_cities = 8
    cities = generate_cities(num_cities)

    print("Generated cities coordinates:")
    print(cities)
    print()

    graph_a = create_graph(cities, 'a')

    print("Adjacency matrix (Scenario A):")
    print_matrix(graph_a)

    start_city = 0

    print("--- Scenario A ---")

    path_bfs_a, dist_bfs_a = bfs_tsp(graph_a, start_city)
    print("Method: BFS")
    print(f"Path: {path_bfs_a}")
    print(f"Cost: {dist_bfs_a:.2f}\n")

    path_dfs_a, dist_dfs_a = dfs_tsp(graph_a, start_city)
    print("Method: DFS")
    print(f"Path: {path_dfs_a}")
    print(f"Cost: {dist_dfs_a:.2f}\n")

    path_mst_a, dist_mst_a = mst_tsp(graph_a, start_city)
    print("Method: MST")
    print(f"Path: {path_mst_a}")
    print(f"Cost: {dist_mst_a:.2f}\n")

    path_greedy_a, dist_greedy_a = greedy_tsp(graph_a, start_city)
    print("Method: Greedy")
    print(f"Path: {path_greedy_a}")
    print(f"Cost: {dist_greedy_a:.2f}\n")

    graph_b = create_graph(cities, 'b')

    print("Adjacency matrix (Scenario B):")
    print_matrix(graph_b)

    print("--- Scenario B ---")

    path_bfs_b, dist_bfs_b = bfs_tsp(graph_b, start_city)
    print("Method: BFS")
    print(f"Path: {path_bfs_b}")
    if dist_bfs_b == float('inf'):
        print("Cost: inf (Path not found)\n")
    else:
        print(f"Cost: {dist_bfs_b:.2f}\n")

    path_dfs_b, dist_dfs_b = dfs_tsp(graph_b, start_city)
    print("Method: DFS")
    print(f"Path: {path_dfs_b}")
    if dist_dfs_b == float('inf'):
        print("Cost: inf (Path not found)\n")
    else:
        print(f"Cost: {dist_dfs_b:.2f}\n")

    path_mst_b, dist_mst_b = mst_tsp(graph_b, start_city)
    print("Method: MST")
    print(f"Path: {path_mst_b}")
    if dist_mst_b == float('inf'):
        print("Cost: inf (Dead end)\n")
    else:
        print(f"Cost: {dist_mst_b:.2f}\n")

    path_greedy_b, dist_greedy_b = greedy_tsp(graph_b, start_city)
    print("Method: Greedy")
    print(f"Path: {path_greedy_b}")
    if dist_greedy_b == float('inf'):
        print("Cost: inf (Dead end)\n")
    else:
        print(f"Cost: {dist_greedy_b:.2f}\n")

    print("--- Scenario B - Bidirectional Search ---")
    start_bidir = -1
    target_bidir = -1

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            if graph_b[i][j] == float('inf'):
                start_bidir = i
                target_bidir = j
                break
        if start_bidir != -1:
            break

    if start_bidir != -1 and target_bidir != -1:
        print(f"Selected cities: {start_bidir} and {target_bidir}")
        path_bidir, cost_bidir = bidirectional_search(graph_b, start_bidir, target_bidir)
        print("Method: Bidirectional search")
        print(f"Path: {path_bidir}")
        if cost_bidir == float('inf'):
            print("Cost: inf (Path not found)\n")
        else:
            print(f"Cost: {cost_bidir:.2f}\n")
    else:
        print("No missing connections in this specific generation.")


if __name__ == "__main__":
    main()