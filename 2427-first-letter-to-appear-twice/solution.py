class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = {}
        for char in s:
            if char not in a:
                a[char] = 1
            else:
                a[char] += 1
            if a[char] ==2:
                return char
