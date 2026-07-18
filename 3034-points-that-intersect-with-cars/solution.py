class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        seen = set()
        for i in range(len(nums)):
            for j in range(nums[i][0], nums[i][1]+1):
                seen.add(j)
        return len(seen)
