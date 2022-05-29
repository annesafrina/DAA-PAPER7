import sys
from datetime import datetime
import random as r
from queue import PriorityQueue
start_time = datetime.now() 
class Graph:
    def __init__(self, vertex_count):
        self.v = vertex_count
        self.edge = [[-1 for i in range(vertex_count)] for j in range(vertex_count)]
        self.visited_node = []
    def add_edge(self, u, v, weight):
        self.edge[u][v] = weight
        self.edge[v][u] = weight
    def dijkstra(self, start):
        Dijkstra = {v:float('inf') for v in range(self.v)}
        Dijkstra[start] = 0
        pq = PriorityQueue()
        pq.put((0, start))
        while not pq.empty():
            (dist, current) = pq.get()
            self.visited_node.append(current)
            for next in range(self.v):
                if self.edge[current][next] != -1:
                    distance = self.edge[current][next]
                    if next not in self.visited_node:
                        first_weight = Dijkstra[next]
                        second_weight = Dijkstra[current] + distance
                        if second_weight < first_weight:
                            pq.put((second_weight, next))
                            Dijkstra[next] = second_weight
        return Dijkstra
z=9
g = Graph(10)
g.add_edge(0, 1, 2)
g.add_edge(r.randint(0,z),r.randint(0,z),r.randint(0,z))
g.add_edge(r.randint(0,z),r.randint(0,z),r.randint(0,z))
g.add_edge(r.randint(0,z),r.randint(0,z),r.randint(0,z))
g.add_edge(r.randint(0,z),r.randint(0,z),r.randint(0,z))
g.add_edge(r.randint(0,z),r.randint(0,z),r.randint(0,z))
g.add_edge(r.randint(0,z),r.randint(0,z),r.randint(0,z))
g.add_edge(r.randint(0,z),r.randint(0,z),r.randint(0,z))
g.add_edge(r.randint(0,z),r.randint(0,z),r.randint(0,z))
Dijkstra = g.dijkstra(0)
print(Dijkstra)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
