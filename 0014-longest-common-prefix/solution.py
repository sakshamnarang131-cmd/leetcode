class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a = []
        n = float('inf')
        l = len(strs)
        for i in range (0, l):
            n1 = len(strs[i])
            n = min(n, n1)
        count = 1
        s=[]
        if l == 0 or n == 0:
            return "".join(s)
        for j in range(0,n):
            for i in range(0,l-1):
                if strs[i][j] != strs[i+1][j]:
                    count = 0
                    break
                
            if count == 1:
                a.append(strs[0][j])
            else:
                break
        return "".join(a)
