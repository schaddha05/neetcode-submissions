# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v:i for i,v in enumerate(inorder)}
        pre_idx = 0 
        def dfs(l, r):
            nonlocal pre_idx
            if l > r:
                return  
            
            root_val = preorder[pre_idx]
            pre_idx += 1
            root_pos = idx[root_val]
            root = TreeNode(root_val)
            root.left = dfs(l,root_pos -1)
            root.right = dfs(root_pos +1, r)
            return root 
        return dfs(0, len(inorder) -1)


