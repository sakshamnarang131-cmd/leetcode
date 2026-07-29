class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [pow(nums[i],2) for i in range(len(nums))]
        nums.sort()
        return nums
