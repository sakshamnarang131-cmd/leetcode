class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        if n == 100:
            return 100
        if n < 10:
            for i in range(n,10):
                if i%t == 0:
                    return i
        m = max(n,10)
        for i in range(m,101):
            a = (i%10) * (i//10)
            if a%t == 0:
                return i