class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if nums[n-1] < target:
            return n
        for i in range (0, n):
            if nums[i] == target or nums[i] > target:
                return i
