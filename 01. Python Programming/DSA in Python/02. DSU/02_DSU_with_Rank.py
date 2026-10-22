from typing import List

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0]*(n+1)
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def  union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            print(f"{x} and {y} shares the same group")
        else:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x]+=1
    def is_same_set(self, x, y):
        return self.find(x)==self.find(y)

def main():
    number_of_element = int(input())
    dsu = DSU(number_of_element)
    number_of_operation = int(input())
    for _ in range(number_of_operation):
        x, y = map(int, input().split())
        dsu.union(x, y)
    
    number_of_test = int(input())
    for _ in range(number_of_test):
        x, y = map(int, input().split())
        print(f"{x} and {y} are in same set" if dsu.is_same_set(x, y) else f"{x} and {y} are not in same set")

if __name__ == "__main__":
    main()
    
"""

Input:

6
4
1 2
1 4
4 5
5 6
3
1 6
3 6
4 6

Output:

1 and 6 are in same set
3 and 6 are not in same set
4 and 6 are in same set

"""
