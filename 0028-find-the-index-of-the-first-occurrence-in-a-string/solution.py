class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        n1 = len(needle)
        n2 = len(haystack)
        j = 0
        i = 0
        while i < n2:
            if haystack[i] == needle[j]:
                j +=1
                if j == n1:
                    return (i-j+1)
            else:
                i-=j
                j=0
            i+=1
