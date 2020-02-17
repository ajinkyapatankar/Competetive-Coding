class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        nums = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
        for i in range(len(A[0])):
            for j in range(len(A)):
                nums[i][j] = A[j][i]

                
        return nums
        