class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
        if len(s) <3:
            return max(s)
        s.remove(max(s))
        s.remove(max(s))
        return max(s)
