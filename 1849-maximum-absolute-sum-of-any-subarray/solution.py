class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0
        temp_max = 0

        min_sum = 0
        temp_min = 0

        for i in range(len(nums)):
            temp_max += nums[i]
            temp_min += nums[i]
            if temp_max > max_sum:
                max_sum = temp_max
            if temp_max<0:
                temp_max = 0
            if temp_min < min_sum:
                min_sum = temp_min
            if temp_min >0:
                temp_min = 0
        return max(max_sum, abs(min_sum))
