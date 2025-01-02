import heapq

def dijkstra(graph, start):
    # 최단 거리 초기화
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    priority_queue = [(0, start)]  # (거리, 정점)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 정점이면 건너뛰기
        if current_distance > distance[current_node]:
            continue

        # 인접 노드 확인
        for neighbor, weight in graph[current_node]:
            distance_through_current = current_distance + weight
            if distance_through_current < distance[neighbor]:
                distance[neighbor] = distance_through_current
                heapq.heappush(priority_queue, (distance_through_current, neighbor))

    return distance

def main():
    # 그래프 정의 (인접 리스트 형태)
    graph = {
        'A': [('B', 1), ('D', 4)],
        'B': [('C', 2), ('E', 1)],
        'C': [],
        'D': [('E', 3)],
        'E': []
    }

    # 시작 정점
    start = 'A'

    # 다익스트라 알고리즘 실행
    shortest_distances = dijkstra(graph, start)
    
    # 결과 출력
    print("최단 거리:", shortest_distances)

if __name__ == "__main__":
    main()
  
