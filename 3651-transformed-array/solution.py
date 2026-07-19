class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list(nums)
        n = len(nums)
        for i in range(n):
            t = i+nums[i]
            while t>(n-1):
                t-=(n)
            while t <0:
                t+=n
            result[i] = nums[t]
        return result
