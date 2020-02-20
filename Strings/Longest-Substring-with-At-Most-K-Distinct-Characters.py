class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or not k:
            return 0
        
        min_len = 1
        dic = collections.defaultdict()
        left,right = 0,0
        
        while right < len(s):
            dic[s[right]] = right
            right += 1
            
            if len(dic) == k+1:
                min_index = min(dic.values())
                del dic[s[min_index]]
                
                left = min_index + 1
                
            min_len = max(min_len,right - left)
                
        return min_len
                
        