class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TreeNode()
    
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()    
            curr = curr.children[c]

        curr.word = True



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        t = Trie()
        # add all words to trie
        for word in words:
            t.addWord(word)
        
        # dfs backtracking algorithm

        def dfs(r, c, node, word): # node represent current node in trie, word represents word we've built so far
            if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or 
                board[r][c] not in node.children or board[r][c] == '#'):
                return 
            
            # go to next character in word
            node = node.children[board[r][c]]
            temp = board[r][c]
            word += temp
            board[r][c] = '#'

            if node.word:
                res.add(word)
                node.word = False
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            board[r][c] = temp

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c, t.root, '')
        
        return list(res)





