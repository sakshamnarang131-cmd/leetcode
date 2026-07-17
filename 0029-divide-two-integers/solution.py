class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend ==0:
            return 0
        if dividend >0 and divisor >0:
            temp = 1
        elif dividend >0 and divisor <0:
            temp = -1
        elif dividend <0 and divisor >0:
            temp = -1
        elif dividend <0 and divisor <0:
            temp = 1
        result = temp * (abs(dividend) // abs(divisor))

        if result > 2**31 -1:
            return 2**31 -1
        elif result < -2**31:
            return -2**31
        else:
            return result
