class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = "".join([str(nums[i]) for i in range(len(nums))])
        nums = list(nums)
        nums = [int(nums[i]) for i in range(len(nums))]
        return nums
