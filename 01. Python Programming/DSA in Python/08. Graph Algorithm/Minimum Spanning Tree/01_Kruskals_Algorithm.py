from typing import List

class Graph:
    def __init__(self, v:int, nodes:List):
        self.v = v
        self.nodes = nodes
        self.adjList = [[] for _ in range(self.v)]
        self.index = {node:i for i, node in enumerate(nodes)}
        self.node_name = {i:node for i, node in enumerate(nodes)}
        self.parent = [i for i in range(self.v)]
        self.rank = [0]*self.v
    
    def addEdge(self, start:str, end:str, weight:str)->None:
        self.adjList[self.index[start]].append((self.index[end], int(weight)))
    
    def find(self, x:int)->int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x:int, y:int)->bool:
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        else:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
        return True
    
    def kruskals(self)->None:
        all_edges = []
        visited = set()
        
        for vertex in range(self.v):
            for neighbour, weight in self.adjList[vertex]:
                edge = (min(vertex, neighbour), max(vertex, neighbour))
                
                if edge not in visited:
                    visited.add(edge)
                    all_edges.append((weight, vertex, neighbour))
        
        all_edges.sort()
        
        mst = []
        mst_weight = 0
        
        for weight, left, right in all_edges:
            if self.union(left, right):
                mst.append((left, right, weight))
                mst_weight+=weight
            if len(mst) == (self.v-1):
                break
            
        print("\nMinimum Spanning Tree:\n")
        for left, right, weight in mst:
            print(f"{self.node_name[left]}-{self.node_name[right]} = {weight}")
        print(f"\nTotal MST weight: {mst_weight}")
        
def main():
    v, e = map(int, input().split())
    nodes = input().split()
    
    graph = Graph(v, nodes)
    
    for _ in range(e):
        start, end, weight = input().split()
        graph.addEdge(start, end, weight)
        graph.addEdge(end, start, weight)
    
    graph.kruskals()
    
if __name__ == "__main__":
    main()
    
"""

Input:

4 5
A B C D
A B 10
A C 6
A D 5
B D 15
C D 4

Output:


Minimum Spanning Tree:

C-D = 4
A-D = 5
A-B = 10

Total MST weight: 19

"""
