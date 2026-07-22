# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -float('inf')

        def dfs(root):
            nonlocal maxSum
            if not root:
                return 0 
            
            left = dfs(root.left)
            right = dfs(root.right)
            maxCur = max(root.val, root.val + left, root.val + right, root.val + left + right)
            maxSum = max(maxSum, maxCur)

            return max(root.val, root.val + left, root.val + right)
        
        dfs(root)
        return maxSum