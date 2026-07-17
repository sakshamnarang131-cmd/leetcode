class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        a = 0
        while a>9 or a==0:
            a = 0
            while num != 0:
                a += num % 10
                num = num // 10
            num = a

        return a
