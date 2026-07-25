class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False 
        self.index = None 

class Trie:
    def __init__(self):
        self.root = TreeNode()
    
    def addWord(self, word, index):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        
        curr.word = True
        curr.index = index

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        res = set()
        # add all words to trie
        for i in range(len(words)):
            t.addWord(words[i], i)
        

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == '#' 
            or board[r][c] not in node.children):
                return 

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
                node.word = False

            temp = board[r][c]
            board[r][c] = '#'

            dfs(r, c - 1, node, word) # left
            dfs(r, c + 1 , node, word) # right
            dfs(r - 1, c, node, word) # up 
            dfs(r + 1 , c, node, word) # down 

            board[r][c] = temp
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, t.root, '')
        
        return list(res)













