class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        if len(nums) == 1:
            return [0,0]
        count = 0
        for i in range (len(nums)):
            if nums[i] == target:
                for j in range(i, len(nums)):
                    if nums[j] == target:
                        count += 1
                    else:
                        break
                return [i, i+count-1]
