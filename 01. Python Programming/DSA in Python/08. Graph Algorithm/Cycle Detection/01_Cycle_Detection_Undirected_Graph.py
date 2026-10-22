from collections import deque
from typing import List

class UndirectedGraph:
    def __init__(self, v:int, nodes:List):
        self.v = v
        self.nodes = nodes
        self.index = {node:i for i, node in enumerate(nodes)}
        self.inverse_index = {i:node for i, node in enumerate(nodes)}
        self.adjList = [[] for _ in range(self.v)]
    
    def addEdge(self, start, end, weight):
        self.adjList[self.index[start]].append((self.index[end], weight))
    
    def hasCycle(self)->bool:
        visited = [False] * self.v
        for vertex in range(self.v):
            if not visited[vertex]:
                if self.DetectCycle(vertex, -1, visited):
                    return True
        return False    
    def DetectCycle(self, node, parent, visited)->bool:
        visited[node]=True
        for neighbour, weight in self.adjList[node]:
            if parent == neighbour:
                continue
            if visited[neighbour]:
                return True
            if self.DetectCycle(neighbour, node, visited):
                return True
        return False

def main():
    v, e = map(int, input().split())
    nodes = input().split()
    graph = UndirectedGraph(v, nodes)
    
    for _ in range(e):
        start, end, weight = input().split()
        graph.addEdge(start, end, weight)
        graph.addEdge(end, start, weight)
    
    print(graph.hasCycle())

if __name__ == "__main__":
    main()

"""

Input:


5 7
A B C D E
E A 7
A D 60
A C 12
C D 32
C B 20
B A 10
D C 15


Output:

True

"""
