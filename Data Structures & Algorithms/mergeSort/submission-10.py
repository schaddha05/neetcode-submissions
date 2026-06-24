# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        s = 0 
        e = len(pairs) - 1 

        def merge(arr, s, e, m):
            l = arr[s: m+1]
            r = arr[m+1: e + 1]

            i = 0 # left
            j = 0 # right
            k = s # arr

            while i < len(l) and j < len(r):
                if l[i].key <= r[j].key:
                    arr[k] = l[i]
                    i += 1
                else:
                    arr[k] = r[j]
                    j += 1
                
                k += 1
            
            while i < len(l):
                arr[k] = l[i]
                i += 1
                k += 1
            
            while j < len(r):
                arr[k] = r[j]
                j += 1
                k += 1
            
            return arr

        def sort(arr, s, e):
            if e - s + 1 <= 1:
                return arr 
            
            m = (s + e) // 2
            sort(arr,s, m)
            sort(arr, m + 1 , e)

            merge(arr, s, e, m)

            return arr 

        return sort(pairs, s, e)

    
    
        



