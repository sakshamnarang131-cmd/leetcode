class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        count = 0
        for i in range(len(num_str)):
            if num % int(num_str[i]) == 0:
                count+=1
        return count
