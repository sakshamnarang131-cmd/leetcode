class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        final = 0
        for i in range(n):
            final += nums[i] * pow(-1, i)
        return final
