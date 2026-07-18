class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        num.sort()
        num[0] = num[0] + num[3]
        num[1] = num[1] + num[2]
        result = int(num[0]) + int(num[1])
        return result
