class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        m = 0
        for i in range(0,n):
            seen = []
            count = 0
            for j in range (i, n):
                if s[j] not in seen:
                    seen.append(s[j])
                    count += 1
                else:
                    break
            if count > m:
                m = count
                
        return m
