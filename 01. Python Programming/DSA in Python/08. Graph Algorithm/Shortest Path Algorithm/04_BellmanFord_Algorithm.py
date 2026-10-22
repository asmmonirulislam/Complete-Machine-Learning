# 🔹 What is Bellman–Ford?
# Bellman–Ford is a shortest path algorithm that works on graphs with negative edge weights. 
# Unlike Dijkstra, it can detect negative weight cycles too.
# Input: A weighted graph (directed or undirected, but usually directed).
# Output: The shortest distance from a source node to all other nodes (or detect if a negative cycle exists).

# 🔹 Why do we need Bellman–Ford if we already have Dijkstra?
# Dijkstra fails when the graph has negative weights.
# Bellman–Ford handles negative weights.
# But it’s slower → O(V × E) time complexity.
# So:
# Use Dijkstra if weights ≥ 0 (faster).
# Use Bellman–Ford if weights can be negative (safer).


from typing import List

class WeightedGraph:
    def __init__(self, v:int, nodes:List):
        self.v = v
        self.nodes = nodes
        self.adjList = [[] for _ in range(v)]
        self.index = {node:i for i, node in enumerate(nodes)}
    def addEdge(self, start:str, end:str, weight:str):
        self.adjList[self.index[start]].append((self.index[end], int(weight)))
    def BellmanFord(self, source:str)->List:
        distance = [float('inf')]*self.v
        distance[self.index[source]]=0
        
        for _ in range(self.v-1):
            updated=False
            
            for node in range(self.v):
                if distance[node]==float('inf'): continue
                for neighbour, weight in self.adjList[node]:
                    if distance[node]+weight < distance[neighbour]:
                        distance[neighbour]=distance[node]+weight
                        updated=True
            if not updated:
                break
        
        for node in range(self.v):
            if distance[node] == float('inf'): continue
            for neighbour, weight in self.adjList[node]:
                if distance[node]+weight < distance[neighbour]:
                    print(f"Negative Cycle Detected!")
                    return []
        return distance

def main():
    v, e = map(int, input().split())
    nodes = input().split()
    graph = WeightedGraph(v, nodes)
    for _ in range(e):
        start, end, weight = input().split()
        graph.addEdge(start, end, weight)
    source = input()
    print(f"{source}->", end="")
    print(*nodes)
    print("  ",*graph.BellmanFord(source))
    
if __name__=="__main__":
    main()
    
"""
Input:

7 10
A B C D E F G
A B -1
A C 6
A D -2
B E 3
B D 1
C D 5
C F 5
G F -1
E G 3
D F -2
A

Output:

A->A B C D E F G
   0 -1 6 -2 2 -4 5


Input:

5 5
A B C D E
A B 5
B C 2
B D 1
D E 1
E C -1
A

Output:

A->A B C D E
   0 5 6 6 7

"""
