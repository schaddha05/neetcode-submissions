# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        def bfs(node):
            q = deque()
            q.append(node)
            while q:
                levelSize = len(q)
                currLevel = []
                for i in range(levelSize):
                    curr = q.popleft()
                    currLevel.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                res.append(currLevel.pop())
        bfs(root)
        return res
            
        
        dfs(root)
        return res