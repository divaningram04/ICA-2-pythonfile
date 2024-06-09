import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start, end):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        heapq.heapify(priority_queue)
        path = {vertex: None for vertex in self.graph}

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    path[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances[end], self.construct_path(path, start, end)

    def construct_path(self, path, start, end):
        stack = []
        while end is not None:
            stack.append(end)
            end = path[end]
        stack.reverse()
        return stack

g = Graph()

g.add_edge("Port Elizabeth", "East London", 300)
g.add_edge("East London", "Bloemfontein", 460)
g.add_edge("Bloemfontein", "Johannesburg", 400)
g.add_edge("Johannesburg", "Pretoria", 60)
g.add_edge("Port Elizabeth", "George", 320)
g.add_edge("George", "Cape Town", 430)
g.add_edge("Cape Town", "Kimberley", 950)
g.add_edge("Kimberley", "Pretoria", 520)
g.add_edge("East London", "Durban", 660)
g.add_edge("Durban", "Pretoria", 580)
g.add_edge("Durban", "Johannesburg", 570)
g.add_edge("George", "Port Elizabeth", 320)
g.add_edge("Bloemfontein", "Durban", 670)
g.add_edge("George", "Kimberley", 700)
g.add_edge("Johannesburg", "Nelspruit", 330)
g.add_edge("Nelspruit", "Pretoria", 310)
g.add_edge("Port Elizabeth", "Grahamstown", 120)
g.add_edge("Grahamstown", "East London", 130)
g.add_edge("East London", "Durban", 660)
g.add_edge("George", "Knysna", 60)
g.add_edge("Knysna", "Port Elizabeth", 290)
g.add_edge("Kimberley", "Bloemfontein", 170)
g.add_edge("Cape Town", "Johannesburg", 1400)
g.add_edge("Stellenbosch", "Cape Town", 50)
g.add_edge("Stellenbosch", "George", 370)
g.add_edge("Stellenbosch", "Knysna", 420)
g.add_edge("Pietermaritzburg", "Durban", 80)
g.add_edge("Pietermaritzburg", "Johannesburg", 500)
g.add_edge("Mossel Bay", "George", 40)
g.add_edge("Mossel Bay", "Knysna", 110)
g.add_edge("Polokwane", "Pretoria", 260)
g.add_edge("Polokwane", "Johannesburg", 300)
g.add_edge("Rustenburg", "Johannesburg", 110)
g.add_edge("Rustenburg", "Pretoria", 130)
g.add_edge("Umtata", "East London", 230)
g.add_edge("Umtata", "Durban", 420)
g.add_edge("Worcester", "Cape Town", 120)
g.add_edge("Worcester", "Kimberley", 880)
g.add_edge("Springbok", "Cape Town", 560)
g.add_edge("Springbok", "Kimberley", 1000)
g.add_edge("Saldanha", "Cape Town", 140)
g.add_edge("Saldanha", "Stellenbosch", 180)

start_city = "Port Elizabeth"
end_city = "Pretoria"
shortest_distance, shortest_path = g.dijkstra(start_city, end_city)
print(f"Shortest Distance: {shortest_distance} km")
print(f"Shortest Path: {' -> '.join(shortest_path)}")
