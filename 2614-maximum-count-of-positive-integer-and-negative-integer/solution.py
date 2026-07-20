class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_negative = 0
        count_positive = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                count_negative +=1
            if nums[i] >0:
                count_positive +=1
        return max(count_negative, count_positive)
