class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        n = min(nums)
        m = max(nums)
        for i in range(n,m):
            if i not in nums:
                result.append(i)
        return result
