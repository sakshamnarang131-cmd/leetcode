class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        for i in range(len(s)):
            if s[i] == "i":
                a.reverse()
            else:
                a.append(s[i])
        return "".join(a)
