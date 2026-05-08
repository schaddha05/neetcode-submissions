class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False 
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root 
        for c in word:
            node = curr.children.get(c)
            if not node:
                node = TrieNode()
                curr.children.update({c: node})
            curr = node
        curr.endOfString = True 

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            node = curr.children.get(c) 
            if not node:
                return False
            curr = node 

        if not curr.endOfString:
            return False
        else:
            return True 

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            node = curr.children.get(c) 
            if not node:
                return False
            curr = node 
        
        return True