# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def bfs(node):
            if not node:
                return []
            else:
                q = deque()
                q.append(node)
                while q:
                    level_size = len(q)
                    currLevel = []
                    for _ in range(level_size):
                        curr = q.popleft()
                        currLevel.append(curr.val)
                        if curr.left:
                            q.append(curr.left)
                        if curr.right:
                            q.append(curr.right) 
                    res.append(currLevel)
                        

        bfs(root)
        return res