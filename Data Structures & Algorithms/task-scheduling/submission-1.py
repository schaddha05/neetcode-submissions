class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1 
        
        heap = [-x for x in freq.values()] 
        heapq.heapify(heap)
        q = deque() 
        time = 0 
        while heap or q:
            time += 1
            if heap:
                t = 1 + heapq.heappop(heap)
                if t:
                    q.append([t, time + n])

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time

            
            

            

