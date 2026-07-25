class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False 

class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        
        curr.word = True 

    def search(self, word: str) -> bool:
        
        def dfs(index, root):
            curr = root 
            for i in range(index, len(word)):

                if word[i] == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                elif word[i] not in curr.children:
                    return False
                else:
                    curr = curr.children[word[i]]
        
            return curr.word
        
        return dfs(0, self.root)
        
