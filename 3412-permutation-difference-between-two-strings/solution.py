class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        result = 0
        s1 = list(s)
        t1 = list(t)
        for i in range(len(s1)):
            for j in range(len(t1)):
                if s1[i] == t1[j]:
                    result += abs(i-j)
        return result
