from typing import List

class WeightedGraph:
    def __init__(self, v:int, nodes:List):
        self.v = v
        self.nodes = nodes
        self.index = {node:i for i, node in enumerate(nodes)}
        self.distance = [[float('inf')]*self.v for _ in range(self.v)]
        for i in range(self.v):
            self.distance[i][i] = 0
    
    def addEdge(self, start:str, end:str, weight:str)->List:
        self.distance[self.index[start]][self.index[end]]=int(weight)
    
    def FloydWarshal(self)->List:
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    if self.distance[i][k]!=float('inf') and self.distance[k][j]!=float('inf'):
                        self.distance[i][j]=min(self.distance[i][j] , self.distance[i][k]+self.distance[k][j])
        return self.distance
def main():
    v,e = map(int, input().split())
    nodes = input().split()
    graph = WeightedGraph(v, nodes)
    for _ in range(e):
        start, end, weight = input().split()
        graph.addEdge(start, end, weight)
    distance = graph.FloydWarshal()
    print("   ", *nodes)
    for i in range(v):
        print(f"{nodes[i]}->", end=" ")
        for j in range(v):
            print(distance[i][j], end=" ")
        print()
if __name__=="__main__":
    main()
    
    
"""

Input:

4 5
A B C D
A B 5
A D 10
B C 3
C D 1
D A 2
A

Output:

    A B C D
A-> 0 5 8 9 
B-> 6 0 3 4 
C-> 3 8 0 1 
D-> 2 7 10 0 

"""