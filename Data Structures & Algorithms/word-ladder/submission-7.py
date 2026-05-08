from collections import defaultdict
from collections import deque 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def differ_by_one(w1,w2):
            diff = 0 
            for x,y in zip(w1, w2):
                if x != y:
                    diff += 1
            
            return diff == 1
        
        adj = defaultdict(list)
        words = wordList[:]
        if beginWord not in words:
            words.append(beginWord)
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if i != j and differ_by_one(words[i], words[j]):
                    adj[words[i]].append(words[j])
                    adj[words[j]].append(words[i])
        
        q = deque()
        visited = set()
        q.append((beginWord,1))
        visited.add(beginWord)
        while q:
            curr, d = q.popleft()
            if curr == endWord:
                return d
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, d + 1))
        
        return 0



        
