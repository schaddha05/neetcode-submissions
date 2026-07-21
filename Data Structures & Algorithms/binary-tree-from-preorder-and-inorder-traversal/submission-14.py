# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        inorderIndex = {} # every node in inorder to its index 
        for i in range(len(inorder)):
            inorderIndex[inorder[i]] = i
        
        index = 0 # index in preorder array

        def dfs(l, r):
            nonlocal index
            if l > r:
                return None 
            
            node = TreeNode(preorder[index])
            index += 1
            # left subtree
            node.left = dfs(l, inorderIndex[node.val] - 1)
            #right subtree
            node.right = dfs(inorderIndex[node.val] + 1, r)

            return node
        
        return dfs(0, len(inorder) - 1)


            

