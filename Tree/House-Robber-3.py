# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.memo = {}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.search(root)
    
    def search(self,node):
        if node in self.memo:
            return self.memo[node]
        
        if not node:
            return 0
        
        val = 0
        
        if node.left:
            val += self.search(node.left.left) + self.search(node.left.right)
        
        if node.right:
            val+= self.search(node.right.left) + self.search(node.right.right)
            
        val = max(val+node.val,self.search(node.left) + self.search(node.right))
        
        self.memo[node] = val
        
        return self.memo[node]
        