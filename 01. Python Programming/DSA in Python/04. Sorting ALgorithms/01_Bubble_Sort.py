class Sort:
    def bubbleSort(self, arr):
        n = len(arr)
        
        for i in range(0, n-1):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
            
        return arr
    
obj = Sort()

arr = [6, 1, 2, 5, 3, 4, 9, 7, 8]
arr = obj.bubbleSort(arr)
print("Sorted Array: ", *arr)