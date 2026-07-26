class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_product = float('-inf')
        if n == 3:
            return nums[0]*nums[1]*nums[2]
        nums.sort()
        temp = nums[n-1]*nums[n-2]*nums[n-3]
        if temp > max_product:
            max_product = temp
        temp = nums[n-1]*nums[1]*nums[0]
        if temp > max_product:
            max_product = temp
        return max_product
