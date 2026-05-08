from collections import defaultdict
from collections import deque 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 

        adj = defaultdict(list) 
        q = deque()
        visited = set() 

        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adj[pattern].append(word)
        
        q.append((beginWord,1)) 
        visited.add(beginWord)
        while q:
            for i in range(len(q)):
                curr, d = q.popleft()
                if curr == endWord:
                    return d 
                for j in range(len(curr)):
                    pattern = curr[:j] + '*' + curr[j+1:]
                    for neighbor in adj[pattern]:
                        if neighbor not in visited:
                            q.append((neighbor, d+1))
                            visited.add(neighbor)
                    
        return 0






