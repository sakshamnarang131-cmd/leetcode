class Solution(object):
    def limitOccurrences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = 0
        a = []
        for i in range(len(nums)):
            if a.count(nums[i]) != k:
                a.append(nums[i])
        return a
