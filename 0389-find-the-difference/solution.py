class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1 = list(s)
        t1 = list(t)
        for i in range(len(s1)):
            t1.remove(s1[i])
        
        return t1[0]
