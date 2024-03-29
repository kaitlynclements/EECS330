"""
    Author: Kaitlyn Clements
    KUID: 3072622
    Lab: Lab 9- Advanced Graph Algorithms
"""

# A. Implement Dijkstra's Shortest Path Tree Algorithm
# Dijkstra's algorithm is one of the important graph algorithms. It is used to find the shortest path 
# from the source node to other nodes in weighted or directed graph. Priority queue or heap is the data 
# structure that is used to enable such algorithm. In this lab, you can use your own way to implement 
# the minimum distance searching function, such as scaning, sorting, or heap.
import sys 
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dijkstra(self, src):
        # Stores shortest distance.
        dist = [sys.maxsize] * self.V
        # Shortest distance to the same node is 0.
        dist[src] = 0
        
        # Your code.
        # Array to keep track of visited nodes
        visited = [False]*self.V
        
        for _ in range(self.V-1):
            # Find the min distance vertex that has not been visited
            min_dist = sys.maxsize
            min_index = -1           
            for v in range(self.V):
                if not visited[v] and dist[v] < min_dist:
                    min_dist = dist[v]
                    min_index = v                   
            # mark the selected vertex as visited
            visited[min_index] = True            
            # Update the distances of the neighboring vertices
            for neighbor, weight in enumerate(self.graph[min_index]):
                if not visited[neighbor] and weight > 0:
                    new_dist = dist[min_index] + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist        
        # You have to call print_solution by passing dist.
        # In this way everyone's output would be standardized.
        self.print_dijkstra(dist)

    def print_dijkstra(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(f"{node} \t->\t {dist[node]}")

    # B. Implement Prim's Minimum Spanning Tree
    # Prim's algorithm another graph algorithm, that is used to find Minimum Spanning Tree of connected 
    # and unidirectional graph. Minimum Spanning Tree is a subgraph or subset of connected or unidirectional 
    # graph that connects all the vertices together, with no cycles, and while the total edge weight minimal. 
    # Priority queue or heap data structure is typically used to implement Prim's algorithm. Complexity of 
    # O(E + V log V) can be achieved using an efficient implementation. Where, E is number of edges and V is 
    # number of vertices.
    def prim(self):
        # Store the resulting graph.
        # where result[i] keeps the source vertex.
        # See the example output for expected result.
        result = [None] * self.V
        
        # Your code.
        # Initialize key values used to pick min weight edge in cut
        key = [float('inf')]*self.V
        key[0]=0 # Make the first vertex the source of the MST
        
        # Priority queue to store vertices with their key values
        priority_queue = list(range(self.V))
        
        while priority_queue:
            # Find min key vertex in the priority queue
            min_index = min(priority_queue, key=lambda x: key[x])
            u = priority_queue.pop(priority_queue.index(min_index))
            
            for v, weight in enumerate(self.graph[u]):
                if weight > 0 and v in priority_queue and weight < key[v]:
                    key[v] = weight
                    result[v] = u
        
        # You have to call print_solution by passing the output graph.
        # In this way everyone's output would be standardized.
        self.print_prim(result)

    def print_prim(self, result):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print(f"{result[i]} - {i} \t {self.graph[i][result[i]]}")
            


    # C. Kruskal's Minimum Spanning Tree
    # Kruskal's Minimum Spanning Tree is another way to find Minimum Spanning Tree of connected and 
    # unidirectional graph. Kruskal's algorithm uses greedy approach unlike Prim's algorithm, that uses 
    # incremental approach. Disjoint set data structure (that you have previously learned) is used to 
    # implement Kruskal's algorithm to detect existence of circle in MST. Complexity of O(E log E) can be 
    # achieved using an efficient implementation.

    def kruskal_mst(self):
        # Your code.
        # Initialize the resulting MST
        result = []
        
        # Sort all the edges in non-decreasing order of their weight
        edges = []
        for i in range(self.V):
            for j in range(i+1, self.V):
                if self.graph[i][j] > 0:
                    edges.append((i, j, self.graph[i][j]))
        edges.sort(key=lambda x: x[2])
        
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        
        #Helper functions for disjoint set operations
        def find_parent(i):
            if parent[i] == i:
                return i
            return find_parent(parent[i])
        
        def union_sets(i, j):
            root_i = find_parent(i)
            root_j = find_parent(j)
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_i] = root_j
                rank[root_j] += 1
        # Iterate through sorted edges and add to result if it doesn't form a cycle
        for edge in edges:
            u, v, w = edge
            root_u = find_parent(u)
            root_v = find_parent(v)
            if root_u != root_v:
                result.append((u, v, w))
                union_sets(root_u, root_v)
        # Similar to the previous e.g. print your
        # resulting graph.
        self.print_kruskal(result)

    def print_kruskal(self, result):
        print("Edge \t Weight")
        # Note that the below code is slightly different than the Prim's.
        # You can change this print code according to your choice, but
        # you have to display your graph in (vertex->vertex weight) format.
        for edge in result:
            print(f"{edge[0]} -> {edge[1]} \t {edge[2]}")
            

# D. Testing
# Create a graph with 21 vertices.
graph = Graph(21)

# Add edges and their weights.
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 1)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 4, 2)
graph.add_edge(3, 5, 2)
graph.add_edge(4, 6, 2)
graph.add_edge(5, 7, 2)
graph.add_edge(7, 8, 2)
graph.add_edge(6, 8, 2)

graph.add_edge(8, 9, 5)
graph.add_edge(8, 10, 4)
graph.add_edge(9, 11, 3)
graph.add_edge(10, 11, 1)

graph.add_edge(11, 12, 1)
graph.add_edge(12, 13, 1)
graph.add_edge(13, 14, 1)

graph.add_edge(14, 15, 1)
graph.add_edge(14, 16, 10)
graph.add_edge(15, 17, 1)
graph.add_edge(16, 20, 1)
graph.add_edge(17, 18, 1)
graph.add_edge(18, 19, 1)
graph.add_edge(19, 20, 1)

# Run Dijkstra's algorithm from source vertex 0.
graph.dijkstra(0)

# Find and print the Prim's Minimum Spanning Tree (MST).
graph.prim()

# Find and print the Kruskal's Minimum Spanning Tree (MST).
graph.kruskal_mst()