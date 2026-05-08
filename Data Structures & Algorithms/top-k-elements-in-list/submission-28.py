class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [[] for i in range(len(nums)+1)]
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        
        for num, freq in hashmap.items():
            frequencies[freq].append(num)

        result = []
        for i in range(len(frequencies)-1,0,-1):
            for j in range(len(frequencies[i])):
                result.append(frequencies[i][j])
                if len(result) == k:
                    return result