class Solution:
    from collections import deque
    import heapq
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = {} # task -> frequency 
        for t in tasks:
            taskFreq[t] = taskFreq.get(t, 0) + 1 
        
        maxHeap = [] # (-frequency, task) since its max heap
        cooldown = deque() # contain (time, task, frequency), front will always contain the next available task in queue 

        for t in taskFreq:
            heapq.heappush(maxHeap,(-taskFreq[t], t)) 
        
        time = 0
        while maxHeap or cooldown: 
            time += 1

            # check if any tasks from cooldown are available again
            if cooldown and time == cooldown[0][0]:
                tm, task, frq = cooldown.popleft() 
                heapq.heappush(maxHeap, (frq, task))
              

            # process most frequent task
            if maxHeap:
                negFreq, task = heapq.heappop(maxHeap)
                negFreq += 1
                if negFreq != 0: # only add to cooldown if tasks remain
                    cooldown.append((time + n + 1, task, negFreq))
        
            else:
                # no tasks available, jump to next available one from cooldown
                if cooldown:
                    time = cooldown[0][0] - 1
        
        return time


            

