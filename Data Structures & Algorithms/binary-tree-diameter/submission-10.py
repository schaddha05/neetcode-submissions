# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0 

        def dfs(node):
            nonlocal max_diameter
            if not node:
                return 0 
            
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            max_diameter = max(max_diameter, leftDepth+ rightDepth)

            return 1 + max(leftDepth, rightDepth)
        
        dfs(root)
        return max_diameter

       