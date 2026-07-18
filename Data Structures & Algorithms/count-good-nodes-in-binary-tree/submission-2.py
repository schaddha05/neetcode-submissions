# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0


        def dfs(root, maxSoFar):
            nonlocal res
            if not root:
                # base case
                return 
            
            if root.val >= maxSoFar:
                res += 1
                maxSoFar = root.val
            
            dfs(root.left, maxSoFar)
            dfs(root.right, maxSoFar)
            

        dfs(root, -float('inf'))
        return res

    