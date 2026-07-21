class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_binary = bin(n)[2:]
        for i in range(len(n_binary)-1):
            if n_binary[i] == n_binary[i+1]:
                return False
        return True
