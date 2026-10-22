from typing import List
from heapq import heappush, heappop

class WeightedGraph:
    def __init__(self, v:int, nodes:List):
        self.v = v
        self.nodes = nodes
        self.adjList = [[] for _ in range(self.v)]
        self.index = {node:i for i, node in enumerate(nodes)}
        
    def addEdge(self, start:str, end:str, weight:int):
        self.adjList[self.index[start]].append((self.index[end], weight))
        
    def Dijkstra(self, source:str)->List:
        distance = [float('inf')]*self.v
        distance[self.index[source]]=0
        pq = [(0, self.index[source])]
        
        while pq:
            current_distance, node = heappop(pq)
            if current_distance > distance[node]: continue
            
            for neighbour, weight in self.adjList[node]:
                new_distance = current_distance+weight
                
                if new_distance < distance[neighbour]:
                    distance[neighbour]=new_distance
                    heappush(pq, (new_distance, neighbour))
        return distance
                    
        

def main():
    v, e = map(int, input().split())
    nodes = input().split()
    graph = WeightedGraph(v, nodes)
    
    for _ in range(e):
        start, end, weight = input().split()
        weight=int(weight)
        graph.addEdge(start, end, weight)
        graph.addEdge(end, start, weight) # undirect
    
    source = input()
    
    print("     ", *nodes, end=" ")
    print("\n", source,"->", end=" ")
    print(*graph.Dijkstra(source), end=" ")

if __name__ == "__main__":
    main()
    
    


"""
Input:

6 8
A B C D E F
A B 1
A C 2
B C 3
B E 4
D E 5
C D 6
E F 8
C F 7
A

Output:

      A B C D E F 
 A -> 0 1 2 8 5 9 
 


Time Complexity: O((V+E)logV)

"""
