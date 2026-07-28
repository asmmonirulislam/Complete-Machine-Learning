class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, x:int)->int:
        if x!= self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x:int, y:int)->bool:
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x==root_y:
            return False
        else:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif(self.rank[root_x]>self.rank[root_y]):
                self.parent[root_y]=root_x
            else:
                self.parent[root_y]=root_x
                self.rank[root_x]+=1
        return True
    
    def detectCycle(self):
        visited = set()
        
        for vertex in range(self.v):
            for neighbour, weight in self.adjList[vertex]:
                edge = (min(vertex, neighbour), max(vertex, neighbour))
                
                if edge not in visited:
                    visited.add(edge)
                    
                    if not self.union(vertex, neighbour):
                        return True
        return False