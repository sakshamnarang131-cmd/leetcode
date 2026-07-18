class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(n):
            count =0 
            for j in range(n):
                if i == int(num[j]):
                    count+=1
            if count != int(num[i]):
                return False
        return True
