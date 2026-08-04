class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s_list = list(s)
        a = []
        for char in s_list:
            if char.lower() in "aeiou":
                a.append(char)
        k = 0
        for i in range(n-1,-1,-1):
            if s_list[i].lower() in "aeiou":
                s_list[i] = a[k]
                k+=1
        return "".join(s_list)
