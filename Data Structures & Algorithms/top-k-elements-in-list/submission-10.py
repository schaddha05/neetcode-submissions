class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        
        arr = []
        for num, freq in hashmap.items():
            arr.append([freq,num])
        arr.sort()

        result = []
        for i in range(len(arr)-1,-1,-1):
            result.append(arr[i][1])
            if len(result) == k:
                return result
