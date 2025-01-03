import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

    def dijkstra(self, start):
        queue = []
        heapq.heappush(queue, (0, start))  # (distance, node)
        distances = {node: float('infinity') for node in self.edges}
        distances[start] = 0
        shortest_path = {}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    shortest_path[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

        return distances, shortest_path

# Example usage
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

distances, paths = graph.dijkstra('A')
print("Distances:", distances)
print("Paths:", paths) 