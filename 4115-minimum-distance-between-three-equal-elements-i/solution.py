class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = set()
        s2 = set()
        s3 = []
        temp = float('inf')
        min_dist = len(nums)
        min_index = 0
        max_index = len(nums)
        for i in range(len(nums)):
            if nums[i] not in s1:
                s1.add(nums[i])
            else:
                if nums[i] not in s2:
                    s2.add(nums[i])
                else:
                    if nums[i] not in s3:
                        s3.append(nums[i])
        count = 1
        for i in range(len(s3)):
            positions = []
            for j in range(len(nums)):
                if nums[j] == s3[i]:
                    positions.append(j)
            for j in range(len(positions) - 2):

                if positions[j+2] - positions[j] < min_dist:
                    min_dist = positions[j+2] - positions[j]
                    temp = s3[i]
        
        if temp in nums:
            return 2*(min_dist)
        else:
            return -1
