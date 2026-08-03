class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        if ord(coordinate1[0]) %2 == 0 and int(coordinate1[1]) %2 ==0:
            a = 0
        elif ord(coordinate1[0]) %2 != 0 and int(coordinate1[1]) %2 !=0:
            a = 0
        else:
            a = 1
        if ord(coordinate2[0]) %2 == 0 and int(coordinate2[1]) %2 ==0:
            b = 0
        elif ord(coordinate2[0]) %2 != 0 and int(coordinate2[1]) %2 !=0:
            b = 0
        else:
            b = 1
        return a==b
