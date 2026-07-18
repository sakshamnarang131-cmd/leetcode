class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        len_n = len(str(n))
        final = 0
        a = 0
        for i in range(len_n):
            a = (n // pow(10, len_n-1-i)) - (n // pow(10, len_n-i))*10
            final += a * pow(-1, i)
        return final
