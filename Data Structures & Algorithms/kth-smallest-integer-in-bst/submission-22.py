# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        kth = None

        def dfs(root, cnt):
            nonlocal kth
            if not root:
                return 
            
            dfs(root.left, cnt)
            if cnt[0] == k:
                kth = root.val
            cnt[0] += 1
            dfs(root.right, cnt)

        dfs(root, [1])
        return kth
