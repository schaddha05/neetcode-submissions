# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       

        def inorder(root, counter):
            if not root:
                return 

            left = inorder(root.left, counter)
            if left is not None:
                return left

            counter[0] += 1
            if counter[0] == k:
                return root.val 
            
            return inorder(root.right, counter)
        
        return inorder(root, [0])
        