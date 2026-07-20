class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        max_sum = 0
        i = 0
        while i<n-1:
            temp = nums[i]
            while (i < n-1) and nums[i+1] > nums[i]:
                i +=1
                temp+=nums[i]
            if temp > max_sum:
                max_sum = temp
            i+=1
        return max_sum
