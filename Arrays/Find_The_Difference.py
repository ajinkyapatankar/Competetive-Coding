class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(s)
        t = list(t)
        
        for ch in s:
            t.remove(ch)
            
        return t[0]