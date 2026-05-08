class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        arr = [[] for i in range(len(nums)+1)]

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        
    
        for num, freq in hashmap.items():
            arr[freq].append(num)
        
        result = []
        for i in range(len(arr)-1,-1,-1):
            for j in range(len(arr[i])):
                result.append(arr[i][j])
                if len(result) == k:
                    return result
