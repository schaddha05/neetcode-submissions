class Solution:
    import heapq
    from collections import deque 
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = {}
        for t in tasks:
            taskFreq[t] = taskFreq.get(t, 0) + 1 
        
        maxHeap = [] # contains [-freq, task]
        cooldown = deque() # contains [time, task, frequency]
        time = 0 
        
        # add all tasks to maxHeap 
        for t in taskFreq:
            heapq.heappush(maxHeap, [-taskFreq[t], t])

        
        while maxHeap or cooldown: 
            time += 1
            
            # put eligible tasks back in maxHeap from cooldown
            if cooldown and time == cooldown[0][0]: 
                time, task, frequency = cooldown.popleft() 
                heapq.heappush(maxHeap, [frequency, task])
            
            # process task with highest current frequency
            if maxHeap:
                frequency, task = heapq.heappop(maxHeap)
                frequency += 1 # adding because they're negative
                if frequency != 0:
                    cooldown.append([time + n + 1, task, frequency])
            else:
                # nothing left in heap, jump to next time of available task
                if cooldown:
                    time = cooldown[0][0] - 1
        
        return time


