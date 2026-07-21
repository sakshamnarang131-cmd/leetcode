class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            count = 0
            i_binary = bin(i)[2:]
            for j in range(len(i_binary)):
                if i_binary[j] == "1":
                    count+=1
            if count == k:
                result+= nums[i]
        return result
