# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        split1 = p.val < root.val and q.val < root.val 
        split2 = p.val > root.val and q.val > root.val 
        if root.val == q.val or root.val == p.val:
            return root
        elif split1: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif split2:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root 


