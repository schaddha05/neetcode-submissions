class FreqStack:
    from collections import defaultdict
    def __init__(self):
        self.maxFreq = 0
        self.freq = defaultdict(int)
        self.group = defaultdict(list)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.maxFreq = max(self.maxFreq, self.freq[val])
        self.group[self.freq[val]].append(val) 

    def pop(self) -> int:
        num = self.group[self.maxFreq][-1] 
        self.freq[num] -= 1
        self.group[self.maxFreq].pop() 
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        
        return num

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()