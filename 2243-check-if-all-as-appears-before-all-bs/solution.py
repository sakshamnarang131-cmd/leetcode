class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b_caught = False
        for i in range(len(s)):
            if s[i] == "b":
                b_caught = True
            if b_caught and s[i] == "a":
                return False
        return True
