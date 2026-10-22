from collections import deque
from typing import List

class DirectedUnweightedGraph:
    def __init__(self, v:int, nodes:List):
        self.v = v
        self.nodes = nodes
        self.index = {node:i for i,node in enumerate(nodes)}
        self.adjList = [[] for _ in range(self.v)]
    
    def addEdge(self, start:str, end:str):
        self.adjList[self.index[start]].append(self.index[end])
    
    def bfs_shortest_path(self, source:str)->List:
        q = deque()
        visited = [False]*self.v
        distance = [-1]*self.v
        
        visited[self.index[source]]=True
        distance[self.index[source]]=0
        
        q.append(self.index[source])
        
        while q:
            node = q.popleft()
            for i in self.adjList[node]:
                if not visited[i]:
                    visited[i]=True
                    distance[i]=distance[node]+1
                    q.append(i)
        return distance
    
    


def main():
    v, e = map(int, input().split())
    nodes = input().split()
    
    graph = DirectedUnweightedGraph(v, nodes)
    
    for _ in range(e):
        start, end = input().split()
        graph.addEdge(start, end)
        graph.addEdge(end, start)   # undirected

    source = input()
    print("     ", *nodes, end=" ")
    print("\n", source,"->", end=" ")
    print(*graph.bfs_shortest_path(source), end=" ")

if __name__ == "__main__":
    main()
    
    
"""
Input:


6 9
A B C D E F
A B
A F
B F
B E
E F
E D
B D
B C
C D
A

Output:

      A B C D E F 
 A -> 0 1 2 2 2 1 

"""
