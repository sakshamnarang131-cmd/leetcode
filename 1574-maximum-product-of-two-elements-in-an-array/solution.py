class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_mul = float('-inf')
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!= j:
                    if (nums[i]-1)*(nums[j]-1) > max_mul:
                        max_mul = (nums[i]-1)*(nums[j]-1)
        return max_mul
