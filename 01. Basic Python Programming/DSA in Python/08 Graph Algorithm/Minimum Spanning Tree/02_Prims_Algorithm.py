from typing import List
from heapq import heappush, heappop

class Graph:
    def __init__(self, v, nodes):
        self.v = v
        self.nodes = nodes
        self.adj = [[] for _ in range(v)]
        self.node_index = {node:i for i, node in enumerate(nodes)}
        self.node_name = {i:node for i, node in enumerate(nodes)}
    
    def addEdge(self, u:str, v:str, w:str)->None:
        self.adj[self.node_index[u]].append((self.node_index[v], int(w)))

        
    def prims(self, start:str)->None:
        
        start = self.node_index[start]
        
        pq = [(0, start, -1)]
        
        visited = set()
        mst = []
        mst_weight = 0
        
        while pq and len(mst) != self.v-1:
            weight, current, parent = heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            
            if parent != -1:
                mst.append((parent, current, weight))
                mst_weight+=weight
            
            for neighbour, weight in self.adj[current]:
                if neighbour not in visited:
                    heappush(pq, (weight, neighbour, current))
        print(f"Minimum Spanning Tree: \n")
        for u, v, w in mst:
            print(f"{self.node_name[u]}-{self.node_name[v]}={w}")
        print()
        print(f"Total Weight: {mst_weight}")
        
    
def main():
    v, e = map(int, input().split())
    nodes = input().split()[:v]
    
    graph = Graph(v, nodes)
    
    for _ in range(e):
        u, v, w = input().split()
        graph.addEdge(u, v, w)
        graph.addEdge(v, u, w)
    
    start = input()
    
    graph.prims(start)

if __name__ == '__main__':
    main()
    
    
"""
Input example:

4 5
A B C D
A B 10
A C 6
A D 5
B D 15
C D 4

Output:

Minimum Spanning Tree: 

A-D=5
D-C=4
A-B=10

Total Weight: 19


"""
