import fractions
class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (2*n)/fractions.gcd(2,n)
