class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if num<0:
                count += 1
            if num==0:
                return 0
        if count%2 == 0:
            return 1
        else:
            return -1
