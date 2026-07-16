class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import fractions
        mxi = nums[0]
        n = len(nums)
        prefixgcd = []
        for i in range (0,n):
            if nums[i] > mxi:
                mxi = nums[i]
            prefixgcd.append(fractions.gcd(nums[i], mxi))
        prefixgcd.sort()
        n = len(prefixgcd)
        s = 0
        for i in range (0, n//2):
            s += fractions.gcd(prefixgcd[i], prefixgcd[n-1-i])
        return s
