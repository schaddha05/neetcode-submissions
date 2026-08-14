# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True 
            
            # structure not the same
            if p and not q:
                return False
            elif q and not p:
                return False 
            
            if p.val != q.val:
                return False 
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def dfs(root): 
            if not root:
                return False 
            
            if root.val == subRoot.val and isSameTree(root, subRoot):
                return True
            
            return dfs(root.left) or dfs(root.right) 
        
        return dfs(root)




    
    