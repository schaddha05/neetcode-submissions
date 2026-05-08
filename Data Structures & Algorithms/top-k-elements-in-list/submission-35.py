class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = {}
        res = []

        for num in nums: 
            freq[num] = freq.get(num, 0) + 1 
        
        for key in freq:
            buckets[freq[key]].append(key)
        
        for i in range(len(buckets) -1, 0, -1):
            if len(buckets[i]) > 0:
                for j in range(len(buckets[i])):
                    res.append(buckets[i][j])
                    if len(res) == k:
                        return res

