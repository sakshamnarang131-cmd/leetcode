class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(1, len(s)):
            if abs(ord(s[i]) - ord(s[i-1])) != 0 and abs(ord(s[i]) - ord(s[i-1])) != 32:
                result +=1
        return result
