class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        
        arr = []

        for num, cnt in hashmap.items():
            arr.append([cnt, num])
        arr.sort()

        result = []
        for i in range(k):
            result.append(arr.pop()[1])
        
        return result





       
                
            
