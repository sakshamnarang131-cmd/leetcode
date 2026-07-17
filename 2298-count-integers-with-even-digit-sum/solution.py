class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for i in range(1,num+1):
            tempo = i
            temp = 0
            for j in range(len(str(num))):
                temp += tempo % 10
                tempo = tempo // 10
            tempo = temp
            if temp %2 == 0:
                count += 1
        return count
