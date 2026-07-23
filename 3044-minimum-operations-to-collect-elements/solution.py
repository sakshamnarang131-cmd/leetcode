class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        collection = set()
        result = 0
        for i in range(len(nums)-1,-1,-1):
            result +=1
            if nums[i] <= k:
                collection.add(nums[i])
            
            if len(collection) == k:
                break
            
        return result
