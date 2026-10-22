class DirectedWeightedGraph:
    def __init__(self, v, nodes):
        self.v = v
        self.nodes = nodes
        self.adjMat = [[0]*v for _ in range(v)]
        self.index = {node:i for i, node in enumerate(nodes)}
        self.reverse_index = {i:node for i, node in enumerate(nodes)}
    
    def add_edge(self, start, end, weight):
        self.adjMat[self.index[start]][self.index[end]]=weight
    
    def display(self):
        print(" ", *self.nodes, end=" ")
        print()
        indx = 0
        for row in self.adjMat:
            print(self.reverse_index[indx], end=" ")
            indx+=1
            for val in row:
                print(val, end=" ")
            print()




def main():
    v, e = map(int, input().split())
    nodes = input().split()
    
    graph = DirectedWeightedGraph(v, nodes)
    
    for i in range(e):
        start, end, weight = input().split()
        graph.add_edge(start, end, weight)
    
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

  A B C D E 
A 0 0 12 60 0 
B 10 0 0 0 0 
C 0 20 0 32 0 
D 0 0 15 0 0 
E 7 0 0 0 0 

"""
