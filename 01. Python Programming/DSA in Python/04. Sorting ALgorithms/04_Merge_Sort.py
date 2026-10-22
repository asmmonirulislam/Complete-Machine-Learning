class Sort:
    def mergeSort(self, arr):
        n = len(arr)
        if n<=1: return arr
        mid = n//2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        
        if left[-1]<=right[0]:
            return left+right
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        arr = []
        i = j = 0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                arr.append(left[i])
                i+=1
            else:
                arr.append(right[j])
                j+=1
                
        arr.extend(left[i:])
        arr.extend(right[j:])
        
        return arr

obj = Sort()
arr = [5,1,8,2,4,3,9,7,6]
sorted_arr = obj.mergeSort(arr)
print(sorted_arr)