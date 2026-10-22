class Sort:
    def selectionSort(self, arr):
        n = len(arr)
        
        for i in range(n-1):
            min_index = i
            
            for j in range(i+1, n):
                if arr[j]<arr[min_index]:
                    min_index=j
                    
            if not min_index==i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
                
obj = Sort()
arr = [5,1,8,2,4,3,9,7,6]
sorted_arr = obj.selectionSort(arr)
print(sorted_arr)