class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for idx,num in enumerate (nums):
            if (target - num) not in dict:
                dict[num] = idx
            else:
                return dict[target-num],idx
        
        
        