class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        result = 0
        for i in range(left, right+1):
            count = 0
            i_binary = bin(i)[2:]
            for j in range(len(i_binary)):
                if i_binary[j] == "1":
                    count+=1
            if count == 2 or count == 3 or count == 5 or count == 7 or count == 11 or count == 13 or count == 17 or count == 19:
                result +=1
        return result
