class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        if n%2 != 0:
            for i in range(-1*(n//2), -1*(n//2) + n):
                result.append(i)
        else:
            for i in range(1-n, n, 2):
                result.append(i)
        return result
