# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = -float('inf')

        def dfs(root):
            nonlocal maxDiam
            if not root:
                return 0 
            
            left = dfs(root.left)
            right = dfs(root.right)
            diam = left + right
            maxDiam = max(maxDiam, diam)
            return 1 + max(left, right)
        
        dfs(root)
        return maxDiam
