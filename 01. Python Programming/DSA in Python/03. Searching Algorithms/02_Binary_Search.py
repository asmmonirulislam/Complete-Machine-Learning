class Search:
    def binarySearch(self, arr, target):
        left = 0
        right = len(arr)-1
        while(left<=right):
            mid = (left+right)//2
            
            if arr[mid]==target:
                print(f"{target} found at location {mid}")
                return
            elif target > arr[mid]:
                left = mid+1
            else:
                right = mid-1
        print(f"{target} not found!")

obj = Search()
arr = [1, 3, 5, 7, 9, 13]
target1 = 7
target2 = 8
obj.binarySearch(arr, target1) # 7 found at location 3
obj.binarySearch(arr, target2) # 8 not found!


# Time Complexity: O(log n)
# Space Complexity: O(1)