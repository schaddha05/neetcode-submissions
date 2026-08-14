# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        smaller = min(p.val, q.val)
        bigger = max(p.val, q.val)

        def dfs(root):
            nonlocal smaller
            nonlocal bigger

            if not root:
                return 
            
            if root.val >= smaller and root.val <= bigger:
                return root 
            
            if root.val > bigger: 
                return dfs(root.left)
            else:
                return dfs(root.right)
        
        return dfs(root)
        
         