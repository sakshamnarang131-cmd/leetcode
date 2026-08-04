class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        max_count= 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count+=1
            else:
                count = 1
            if max_count < count:
                max_count = count
        return max_count
