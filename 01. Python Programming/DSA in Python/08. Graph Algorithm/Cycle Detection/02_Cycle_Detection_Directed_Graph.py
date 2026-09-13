class DirectedGraph:
    def __init__(self, v, nodes):
        self.v = v
        self.nodes = nodes
        self.index = {node:i for i,node in enumerate(nodes)}
        self.adjList = [[] for _ in range(self.v)]
    
    def addEdge(self, start, end, weight):
        self.adjList[self.index[start]].append((self.index[end], weight))
    
    def hasCycle(self):
        visited = [False]*self.v
        recStack = [False]*self.v
        for vertex in range(self.v):
            if not visited[vertex]:
                if self.detectCycle(vertex, visited, recStack):
                    return True
        return False

    def detectCycle(self, vertex, visited, recStack):
        visited[vertex]=True
        recStack[vertex]=True
        
        for neighbour, weight in self.adjList[vertex]:
            if not visited[neighbour]:
                if self.detectCycle(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour] is True:
                return True
        
        recStack[vertex]=False
        return False
    


def main():
    v, e = map(int, input().split())
    nodes = input().split()
    
    graph = DirectedGraph(v, nodes)
    
    for _ in range(e):
        start, end, weight = input().split()
        graph.addEdge(start, end, weight)
    
    print("Cycle Detected!") if graph.hasCycle() else print("No Cycle Detected!")
    

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

"""
