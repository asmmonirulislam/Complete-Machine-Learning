class Search:
    def linearSearch(self, arr, target):
        for i, num in enumerate(arr):
            if num==target:
                print(f"{target} found at location {i}")
                return
        print(f"{target} not found")

obj = Search()
arr = [5, 1, 2, 4, 3, 7, 8, 6]
target1 = 10
target2 = 7
obj.linearSearch(arr, target1) # 10 not found
obj.linearSearch(arr, target2) # 7 found at location 5

# Time Complexity: O(n)
# Space Complexity: O(1)