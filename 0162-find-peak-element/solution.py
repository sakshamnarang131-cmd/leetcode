class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        for i in range(n):
            if i == 0:
                if nums[i] >= nums[i+1]:
                    return i
            elif i == n-1:
                if nums[i] >= nums[i-1]:
                    return i
            else:
                if nums[i] >= nums[i-1] and nums[i]>= nums[i+1]:
                    return i
