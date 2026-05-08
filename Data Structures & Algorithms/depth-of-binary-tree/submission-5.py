# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        longest = 0 
        def dfs(node, curr):
            nonlocal longest
            if not node:
                return 
            
            curr += 1
            if not node.left and not node.right:
                longest = max(curr, longest)
            
            dfs(node.left, curr)
            dfs(node.right, curr)
        
        dfs(root, 0)
        return longest
                