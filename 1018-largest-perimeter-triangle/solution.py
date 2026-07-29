class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        max_peri = 0
        for i in range(n-1,1,-1):
            if nums[i] < nums[i-1] + nums[i-2]:
                peri = nums[i] + nums[i-1] + nums[i-2]
                if peri > max_peri:
                    max_peri = peri
        return max_peri
