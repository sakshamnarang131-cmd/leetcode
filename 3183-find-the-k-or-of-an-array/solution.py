class Solution(object):
    def findKOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        m = max(nums)
        m_binary = bin(m)[2:]
        for i in range(len(nums)):
            nums_binary = bin(nums[i])[2:]
            nums[i] = nums_binary

        for i in range(len(nums)):
            for j in range(len(m_binary) - len(nums[i])):
                nums[i] = "0"+nums[i]
                
        a = ""
        count = 0
        for i in range(len(m_binary)):
            count = 0
            for j in range(len(nums)):
                if nums[j][i] == "1":
                    count+=1
            if count >= k:
                a = a+"1"
            else:
                a = a+"0"

        return int(a,2)
