# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        if not root: return []
        ans = []
        while queue:
            size = len(queue)
            ans.append([])
            for i in range(size):
                node = queue.pop(0)
                ans[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return ans
                
                
        