class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 6 ==0:
                result += nums[i]
                count+=1
        if count == 0:
            return 0
        return result/count
