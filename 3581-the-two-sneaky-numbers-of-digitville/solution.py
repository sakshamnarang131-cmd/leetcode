class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        seen = set()
        for i in nums:
            if i in seen:
                result.append(i)
            else:
                seen.add(i)
        return result
