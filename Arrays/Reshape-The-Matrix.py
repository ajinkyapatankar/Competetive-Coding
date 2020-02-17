class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nums_ = [i for num in nums for i in num]
        if r*c != len(nums_):
            return nums
        
        ans = []
        r_count = 0
        while r_count < r:
            ans.append(nums_[r_count*c:r_count*c+c])
            r_count += 1
            
        return ans