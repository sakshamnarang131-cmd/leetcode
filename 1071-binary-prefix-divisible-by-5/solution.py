class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        a = []
        a.append(nums[0])
        n = len(nums)
        temp = nums[0]
        for i in range(1,n):
            a.append(2*temp + nums[i])
            temp = a[i]
            a[i] = (a[i]%5 == 0)
        a[0] = (a[0]%5 == 0)
        return a
