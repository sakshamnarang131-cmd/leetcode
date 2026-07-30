class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        a = []
        for i in range(len(nums)):
            if nums[i] >0:
                a.append(nums[i])
        for i in range(1,len(a)+1):
            if i != a[i-1]:
                return i
        if len(a) == 0:
            return 1
        return a[-1]+1
