class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 

        for key in freq:
            buckets[freq[key]].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        