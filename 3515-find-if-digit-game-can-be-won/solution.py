class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        single = 0
        double = 0
        for i in range(len(nums)):
            if nums[i] < 10:
                single += nums[i]
            else:
                double += nums[i]
        if single == double:
            return False
        else:
            return True
