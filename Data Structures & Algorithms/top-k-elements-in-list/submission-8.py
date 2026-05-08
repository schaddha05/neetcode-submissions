class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        arr = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for num in hashmap.keys():
            arr[hashmap[num]].append(num)
        
        result = []
        for i in range(len(arr)-1,0,-1):
            for n in arr[i]:
                result.append(n)
                if len(result) == k:
                    return result









       
                
            
