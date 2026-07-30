class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        n = len(nums)
        nums_set = set(nums)
        for i in range(1,n+1):
            if i not in nums_set:
                result.append(i)
        return result

