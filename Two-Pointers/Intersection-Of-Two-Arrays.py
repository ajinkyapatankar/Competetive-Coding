class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_num = {}
        a = []
        for i in nums1:
            if i not in dict_num:
                dict_num[i] = 1
            
        for i in nums2:
            if i in dict_num:
                a.append(i)
                del dict_num[i]
                
        return a
            
        