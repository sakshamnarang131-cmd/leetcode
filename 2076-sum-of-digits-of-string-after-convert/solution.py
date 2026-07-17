class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        a = []
        for i in range(len(s)):
            a.append(ord(s[i])-96)
        a = int("".join([str(a[i]) for i in range(len(a))]))
        for i in range(k):
            temp = 0
            while a != 0:
                temp += a % 10
                a = a // 10
            a = temp
        return temp
