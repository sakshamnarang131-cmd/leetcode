class Solution(object):
    def reverseByType(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = []
        b = []
        for i in range(len(s)):
            if s[i].isalpha():
                a.append(s[i])
        for i in range(len(s)):
            if s[i].isalpha():
                pass
            else:
                b.append(s[i])
        k = len(a)-1
        j = len(b)-1
        result = []
        for i in range(len(s)):
            if s[i].isalpha():
                result.append(a[k])
                k-=1
            else:
                result.append(b[j])
                j-=1
        return "".join(result)
