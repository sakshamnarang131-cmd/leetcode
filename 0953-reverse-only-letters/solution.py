class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 100% runtime
        a = []
        for i in range(len(s)):
            if s[i].isalpha():
                a.append(s[i])
        k = len(a)-1
        result = []
        for i in range(len(s)):
            if s[i].isalpha():
                result.append(a[k])
                k-=1
            else:
                result.append(s[i])
        return "".join(result)
