class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        least = float('inf')
        n = len(nums)

        for i in range (0,n-2):
            j = i+1
            k = n-1
            while j < k:
                sum_num = nums[i] + nums[j] + nums[k]
                diff = abs(sum_num - target)

                if diff < abs(least-target):
                    least = sum_num
                if sum_num < target:
                    j += 1
                else:
                    k -= 1
        return least
