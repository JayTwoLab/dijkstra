import heapq

def dijkstra(graph, start):
    # Initialize shortest distance
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    priority_queue = [(0, start)]  # (Distance, Vertex)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if already processed vertices
        if current_distance > distance[current_node]:
            continue

        # Verifying Adjacent Nodes
        for neighbor, weight in graph[current_node]:
            distance_through_current = current_distance + weight
            if distance_through_current < distance[neighbor]:
                distance[neighbor] = distance_through_current
                heapq.heappush(priority_queue, (distance_through_current, neighbor))

    return distance

def main():
    # Graph definition (adjacent list format)
    graph = {
        'A': [('B', 1), ('D', 4)],
        'B': [('C', 2), ('E', 1)],
        'C': [],
        'D': [('E', 3)],
        'E': []
    }

    # the starting point(vertex)
    start = 'A'

    # Run the Dykstra algorithm
    shortest_distances = dijkstra(graph, start)
    
    # Output Results
    print("the shortest distance:", shortest_distances)

if __name__ == "__main__":
    main()
  
