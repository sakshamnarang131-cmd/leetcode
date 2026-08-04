class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        max_count= 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count+=1
            else:
                count = 1
            if max_count < count:
                max_count = count
        return max_count
