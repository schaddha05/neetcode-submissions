class FreqStack:
    from collections import defaultdict 
    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] += 1

    def pop(self) -> int:
        nums = [] # number(s) with highest frequency
        maxFreq = sorted(list(self.freq.values()))[-1]
        for n in self.freq:
            if self.freq[n] == maxFreq:
                nums.append(n)
        
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] in nums:
                res = self.stack[i]
                self.freq[res] -= 1
                del self.stack[i] 
                return res
        

        



        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()