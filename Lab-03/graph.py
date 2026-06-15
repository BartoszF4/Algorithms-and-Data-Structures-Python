import math
import random


def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def generate_cities(num_cities):
    return [(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(num_cities)]


def create_graph(cities, scenario):
    num_cities = len(cities)
    graph = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                graph[i][j] = calculate_distance(cities[i], cities[j])

    if scenario == 'b':
        edges = []
        for i in range(num_cities):
            for j in range(i + 1, num_cities):
                edges.append((i, j))

        num_edges_to_remove = int(len(edges) * 0.2)
        edges_to_remove = random.sample(edges, num_edges_to_remove)

        for i, j in edges_to_remove:
            graph[i][j] = float('inf')
            graph[j][i] = float('inf')

    return graph