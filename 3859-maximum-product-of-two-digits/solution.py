class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        list_n = list(str(abs(n)))
        result = float('-inf')
        for i in range(len(list_n)-1):
            for j in range(i+1, len(list_n)):
                if i!=j:
                    temp = int(list_n[i])*int(list_n[j])
                    if temp > result:
                        result = temp
        return result
