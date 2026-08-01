class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = sorted(nums)
        for i in range(len(nums)):
            nums[:] = nums[-1:] + nums[:-1]
            if a == nums:
                return True
        return False
