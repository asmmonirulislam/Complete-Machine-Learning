class DirectedWeightedGraph:
    def __init__(self, v, nodes):
        self.v = v
        self.nodes = nodes
        self.index = {node:i for i, node in enumerate(nodes)}
        self.reversed_index = {i:node for i, node in enumerate(nodes)}
        self.adjList = [[] for _ in range(v)]
    
    def addEdges(self, start, end, weight):
        start = self.index[start]
        self.adjList[start].append((end, weight))
    
    def display(self):
        for i in range(len(self.adjList)):
            print(f"{self.reversed_index[i]} ->", end="")
            
            for j in range(len(self.adjList[i])):
                item, weight = self.adjList[i][j]
                print(f" ({item},{weight})", end='')
                if j < len(self.adjList[i])-1:
                    print(',', end='')
            print()
                

def main():
    v, e = map(int, input().split())
    nodes = input().split()
    
    graph = DirectedWeightedGraph(v, nodes)
    
    for _ in range(e):
        start, end, weight = input().split()
        graph.addEdges(start, end, weight)
    graph.display()
    
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

A -> (D,60), (C,12)
B -> (A,10)
C -> (D,32), (B,20)
D -> (C,15)
E -> (A,7)

"""
