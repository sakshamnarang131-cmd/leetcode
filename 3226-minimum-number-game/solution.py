class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        i = 0
        nums.sort()
        while i<len(nums):
            arr.append(nums[i+1])
            arr.append(nums[i])
            i+=2
        return arr
