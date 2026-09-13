from collections import deque
from typing import List


class UndirectedWeightedGraph:
    def __init__(self, v:int, nodes:List):
        self.v = v
        self.nodes = nodes
        self.index = {node:i for i, node in enumerate(nodes)}
        self.inverse_index = {i:node for i, node in enumerate(nodes)}
        self.adjList = [[] for _ in range(self.v)]
    
    def addEdge(self, start, end, weight):
        self.adjList[self.index[start]].append((self.index[end], weight))
    
    def DFS(self, start):
        ans = []
        s = deque()
        visited = [False] * self.v
        visited[self.index[start]]=True
        s.append(self.index[start])
        
        while s:
            node = s.pop()
            ans.append(self.inverse_index[node])
            for neighbour, weight in self.adjList[node]:
                if not visited[neighbour]:
                    visited[neighbour]=True
                    s.append(neighbour)
        return ans
        
def main():
    v, e = map(int, input().split())
    nodes = input().split()
    graph = UndirectedWeightedGraph(v, nodes)
    
    for _ in range(e):
        start, end, weight = input().split()
        graph.addEdge(start, end, weight)
        graph.addEdge(end, start, weight)
    
    print(*graph.DFS(nodes[0]), end=" ")

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

A B C D E 

"""