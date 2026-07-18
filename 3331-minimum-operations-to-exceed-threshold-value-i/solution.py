class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        final = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] <k:
                final+=1

        return final
