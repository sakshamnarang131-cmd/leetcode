class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        nums_dif = sorted(list(set(nums)))
        d = {}
        j=-1
        count = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                count = 0
                j+=1
            else:
                count += 1
            d[nums_dif[j]] = count+1
        result = 0
        for i in d:
            if d[i] % k ==0:
                result += i*d[i]
                    
        return result
