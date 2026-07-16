class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        s.reverse()
        for i in range (0, len(s)):
            if s[0] == " ":
                s.remove(" ")
            else:
                break
        c = 0
        for i in range (0, len(s)):
            if s[i] != " ":
                c += 1
            elif s[i] == " " or c == len(s):
                break
        return c
