import heapq
from tokenize import endpats


def dijkstra(graph, start, end):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    previous_node = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node =heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node.items()]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_node[neighbor] = current_node
                heapq.heappush(priority_queue,(distance, neighbor))

    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_node[current]
    if path[0] != start:
        return float('inf'), []

    return distances[end], path