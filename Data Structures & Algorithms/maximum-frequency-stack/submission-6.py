class FreqStack:
    from collections import defaultdict 
    def __init__(self):
        self.maxFreq = -float('inf')
        self.freq = defaultdict(int) # num -> freq
        self.group = defaultdict(list) # freq -> stack of nums with that frequency 


    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val) 
        self.maxFreq = max(self.maxFreq, self.freq[val])
        

    def pop(self) -> int:
        num = self.group[self.maxFreq][-1] # element closet to top of stack 
        self.freq[num] -= 1
        self.group[self.maxFreq].pop()
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        
        return num

        

        



        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()