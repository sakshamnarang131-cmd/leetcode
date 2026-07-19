class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        count = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in s:
                count += 1
                if count == 2:
                    return False
            else:
                s.add(nums[i])
                count = 0
            
        return True
