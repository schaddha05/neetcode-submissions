# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return []
        
        q = deque([root])
        while len(q) > 0: 
            levelLen = len(q)
            for i in range(levelLen):
                curr = q.popleft()
                if i == levelLen - 1:
                    res.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return res
