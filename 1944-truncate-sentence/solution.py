class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count = 0
        a = ""
        for i in range(len(s)):
            if s[i] == " ":
                count +=1
            if count == k:
                break
            a += s[i]
        return a
