class Sort:
    def insertionSort(self, arr):
        n=len(arr)
        for i in range(1, n):
            if arr[i-1]<=arr[i]: continue
            key=arr[i]
            j=i-1
            while (j>=0) and (arr[j]>key):
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return arr
    
obj = Sort()
arr = [5,1,8,2,4,3,9,7,6]
sorted_arr = obj.insertionSort(arr)
print(sorted_arr)