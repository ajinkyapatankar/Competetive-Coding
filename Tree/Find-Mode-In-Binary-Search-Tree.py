# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = {}
        queue = [root]
        
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.val in ans:
                    ans[node.val] += 1
                else:
                    ans[node.val] = 1
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        count = sorted(ans.items(), key=lambda item: item[1], reverse=True)
        ref = count[0][1]  
        results = []
        for i in count:
            if i[1] == ref:
                results.append(i[0])
            else:
                break
        return results
        