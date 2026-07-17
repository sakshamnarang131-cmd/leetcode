class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(-31,31):
            if n == pow(2,i):
                return True
        return False
