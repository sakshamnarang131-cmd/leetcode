class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if (x>=0):
            y = str(x)[::-1]
        else:
            y = str(-1*x)[::-1]
        z = 0
        for i in range (len(y)):
            z += int(y[i]) * (10**(len(y) - i-1))
        if (z< (-1*(2**31)) or z> ((2**31)-1)):
            return 0
        if (x>=0):
            return z
        else:
            return -1*z
