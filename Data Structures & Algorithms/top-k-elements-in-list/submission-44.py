class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int) # numbers to frequencies
        for num in nums:
            freqs[num] += 1

        print(freqs)
        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets)
        for num, freq in freqs.items():
            buckets[freq] += [num]
        
        print(buckets)
        res = [] 
        for i in range(len(buckets)-1, 0, -1):
            j = len(buckets[i]) - 1
            while j >= 0:
                if k == 0:
                    break 
                res.append(buckets[i][j])
                k -= 1
                j -= 1
                
        return res



