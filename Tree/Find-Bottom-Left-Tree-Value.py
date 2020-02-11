# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = []
        
        if not root:
            return 0
        queue = [root]
        while queue:
            ans.append([])
            for i in range(len(queue)):
                node = queue.pop(0)
                
                ans[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return ans[-1][0]
                
        