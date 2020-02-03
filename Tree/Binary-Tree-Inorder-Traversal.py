# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root,res)
        return res
    
    def helper(self,node,res):
        if node:
            self.helper(node.left,res)
            res.append(node.val)
            self.helper(node.right,res)
            