class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        for x in range(int(pow(n,0.34))+3):
            if n == pow(3,x):
                return True
        return False
