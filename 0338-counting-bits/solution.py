class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n+1):
            i_binary = bin(i)[2:]
            count = 0
            for j in range(len(i_binary)):
                if i_binary[j] == "1":
                    count+=1
            result.append(count)
        return result
