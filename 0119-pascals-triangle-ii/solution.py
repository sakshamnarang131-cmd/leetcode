class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows = rowIndex +1
        result = []
        for i in range(1,numRows+1):
            result.append([1]*i)
        if numRows == 1:
            return [1]
        elif numRows == 2:
            return [1,1]
        for i in range(2,numRows):
            for j in range(1,i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        return result[rowIndex]
