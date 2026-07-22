class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                target = nums[i-1] + 1
                result += target - nums[i]
                nums[i] = target
        return result
