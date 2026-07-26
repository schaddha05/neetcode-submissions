# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, curSum):
            if not root:
                return False
            
            curSum[0] += root.val
            if not root.left and not root.right and curSum[0] == targetSum:
                return True 
            
            left = dfs(root.left, curSum)
            right = dfs(root.right, curSum)

            if left or right:
                return True
            
            curSum[0] -= root.val
            return False 
        
        return dfs(root, [0])