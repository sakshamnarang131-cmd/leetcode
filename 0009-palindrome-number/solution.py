class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l = list(str(x))
        for i in range (0,len(l)):
            if l[i] == l[len(l)-1-i]:
                a = 1
            else:
                a = 0
                break
        return a == 1
