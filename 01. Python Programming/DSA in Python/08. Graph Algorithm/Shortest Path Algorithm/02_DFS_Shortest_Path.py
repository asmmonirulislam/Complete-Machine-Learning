# Need to fix the code


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
    
    
    def dfs_shortest_path(self, source:str)->List:
        visited = [False]*self.v
        distance = [-1]*self.v
        
        s = deque()
        
        visited[self.index[source]]=True
        distance[self.index[source]]=0
        
        s.append(self.index[source])
        
        while s:
            node = s.pop()
            
            for i in self.adjList[node]:
                if not visited[i]:
                    visited[i]=True
                    distance[i]=distance[node]+1
                    s.append(i)
                else:
                    if distance[i] > (distance[node]+1):
                        distance[i] = distance[node]+1
                        s.append(i)
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
    print(*graph.dfs_shortest_path(source), end=" ")

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
