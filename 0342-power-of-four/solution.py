class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        for x in range(int(pow(n,0.25))+2):
            if n == pow(4,x):
                return True
        return False
