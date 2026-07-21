class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        binary_str = bin(n)[2:]
        for i in range(len(binary_str)):
            if binary_str[i] == "1":
                count+=1
        return count
