import heapq

import networkx as nx
import matplotlib.pyplot as plt


#TODO Створення власного вагового графа (Наданий приклад не підходить для перевірки роботи алгоритму)
G = nx.Graph()
G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=2)
G.add_edge("B", "C", weight=1)
G.add_edge("B", "D", weight=5)
G.add_edge("C", "D", weight=8)
G.add_edge("C", "E", weight=10)
G.add_edge("D", "E", weight=2)
G.add_edge("D", "Z", weight=6)
G.add_edge("E", "Z", weight=3)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph.nodes}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    visited = set()
    while priority_queue:
        # Реалізація алгоритму Дейкстри використовуючи бінарну купу
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "A")
print("Найкоротші відстані від вершини A:")
for vertex, distance in shortest_paths.items():
    print(f"A -> {vertex}: {distance}")

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=15)

plt.title("Ваговий граф для демонстрації алгоритму Дейкстри")
plt.axis("off")
plt.show()
