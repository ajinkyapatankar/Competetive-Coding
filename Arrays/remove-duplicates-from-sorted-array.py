class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for v in nums:
            if i==0 or v>nums[i-1]:
                nums[i] = v
                i += 1
        
        return i
        