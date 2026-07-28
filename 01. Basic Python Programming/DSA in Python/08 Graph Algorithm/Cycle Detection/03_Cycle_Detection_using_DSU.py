from typing import List

class Graph:
    def __init__(self, v:int, nodes:List):
        self.v = v
        self.nodes = nodes
        self.adjList = [[] for _ in range(self.v)]
        self.index = {node:i for i, node in enumerate(nodes)}
        self.parent = [i for i in range(self.v)]
        self.rank = [0]*self.v
    
    def addEdge(self, start:str, end:str, weight:str):
        self.adjList[self.index[start]].append((self.index[end], int(weight)))
        
    def find(self, x:int)->int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x:int, y:int)->bool:
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x ==  root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_y] > self.rank[root_x]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True
            
    def DetectCycle(self)->bool:
        visited = set()
        
        for vertex in self.adjList:
            for neighbour, weight in self.adjList[vertex]:
                edge = (min(vertex, neighbour), max(vertex, neighbour))
                
                if edge not in visited:
                    visited.add(edge)
                    
                    if not self.union(vertex, neighbour):
                        return True
        return False
    
    
def main():
    v, e = map(int, input().split())
    nodes = input().split()[:v]
    graph = Graph(v, nodes)
    
    for _ in range(e):
        start, end, weight = input().split()
        graph.addEdge(start, end, weight)
        graph.addEdge(end, start, weight)  #undirected
    
    print("Cycle Detected" if graph.DetectCycle() else "No Cycle Detected")
    
if __name__ == "__main__":
    main()

