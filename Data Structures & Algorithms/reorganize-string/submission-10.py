class Solution:
    from collections import defaultdict
    import heapq
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int) 
        for c in s:
            freq[c] += 1
        
        for c in freq:
            if freq[c] > (len(s) + 1) // 2:
                return ""
        
        res = ""
        maxHeap = []
        for c in freq:
            maxHeap.append([-freq[c], c])
        
        heapq.heapify(maxHeap)
        prev = None 
        while maxHeap:
            frq, c = heapq.heappop(maxHeap)
            res += c
            if prev != None:
                heapq.heappush(maxHeap, prev)
            frq += 1
            if frq != 0:
                prev = [frq, c]
            else:
                prev = None
            
        
        return res


