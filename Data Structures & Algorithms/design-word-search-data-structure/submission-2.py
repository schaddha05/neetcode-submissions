class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False 
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root 
        for c in word:
            node = curr.children.get(c) 
            if not node:
                node = TrieNode() 
                curr.children.update({c: node})
            curr = node 
        curr.endOfWord = True 

    def search(self, word: str) -> bool:
       
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True 
                    return False
                else:
                    node = curr.children.get(c) 
                    if not node:
                        return False 
                    curr = node
            
            return curr.endOfWord
        
        return dfs(0, self.root)