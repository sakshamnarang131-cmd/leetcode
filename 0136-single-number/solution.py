class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = []
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
            else:
                seen.remove(nums[i])
        return seen[0]
