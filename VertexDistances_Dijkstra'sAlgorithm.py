# %%
import heapq
file = r'C:\Users\mratk\Downloads\Project4In.txt'

try:
    with open(file, 'r') as f:
        data = f.read().split()

        integers = [int(num) for num in data]

except FileNotFoundError:
    print("File not found")

def dijkstra(G, source, vertices_count):
    distances = [float('inf')] * (vertices_count + 1)
    previous_vertex = [-1] * (vertices_count + 1)
    distances[source] = 0
    queue = [(0, source)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for next, weight in G[current_vertex]:
            distance = current_distance + weight
            if distance < distances[next]:
                distances[next] = distance
                previous_vertex[next] = current_vertex
                heapq.heappush(queue, (distance, next))
    return distances, previous_vertex


def vertex_path(previous_vertex, source, end):
    path = []
    current = end
    while current != -1:
        path.append(current)
        if current == source:
            return path[::-1]
        current = previous_vertex[current]
    return None

def G_data(input):
    lines = input.strip().splitlines()
    if not lines: return []

    vertices_count, edges_count = map(int, lines[0].split())

    G = [[] for _ in range(vertices_count + 1)]

    for i in range(1, edges_count + 1):
        first, last, _ = map(int, lines[i].split())
        G[first].append((last, _))

    results = []
    for i in range(1, vertices_count + 1):
        distances, previous_vertex = dijkstra(G, i, vertices_count)
        for end in range(1, vertices_count + 1):
            if i == end:
                results.append(f"Shortest path {i} to {end}: Distance 0, Path: [{i}]")
                continue

            path_list = vertex_path(previous_vertex, i, end)
            if path_list:
                path_string = " -> ".join(map(str, path_list))
                results.append(f"Shortest path from {i} to {end}: Distance {distances[end]}, Path: [{path_string}]")
            else:
                results.append(f"Shortest path from {i} to {end}: No path exists.")
    return results

def read_graphs(file):
    with open("Project4In.txt", 'r') as f:
        integers = f.read().strip()

    graphs = integers.split('\n\n')
    results = []
    for graph in graphs:
        if graph.strip():
            results.extend(G_data(graph))
    return results

results = read_graphs(file)
for line in results:
    print(line)