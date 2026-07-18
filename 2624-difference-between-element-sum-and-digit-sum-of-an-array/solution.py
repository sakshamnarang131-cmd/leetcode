class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_sum = sum(nums)
        digit_sum = 0

        nums = [str(nums[i]) for i in range (len(nums))]
        nums = "".join(nums)
        for i in range(len(nums)):
            digit_sum += int(nums[i])
        return abs(element_sum - digit_sum)
