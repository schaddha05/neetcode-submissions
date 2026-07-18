# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0

        def dfs(root):
            nonlocal maxDiam
            if not root:
                return 0 
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            d = left_height + right_height
            maxDiam = max(maxDiam, d)
            
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return maxDiam

