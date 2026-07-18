class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        final = 0
        for i in range(len(nums)):
            count = 0
            while nums[i] != 0:
                nums[i] = nums[i] // 10
                count +=1
            if count % 2 == 0:
                final += 1
        return final
