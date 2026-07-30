class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if len(nums) == 1:
            return sorted(nums[0])
        for j in range(len(nums[0])):
            count = 0
            for i in range(1, len(nums)):
                if nums[0][j] in nums[i]:
                    count += 1
                if count == (len(nums) - 1):
                    result.append(nums[0][j])
        return sorted(result)
