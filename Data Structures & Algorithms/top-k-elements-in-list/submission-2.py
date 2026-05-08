class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = count.get(num,0) + 1 
        
        for num, cnt in count.items():
            arr[cnt].append(num)
      
        result = []

        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                result.append(n)
                if len(result) == k:
                    return result




       
                
            
