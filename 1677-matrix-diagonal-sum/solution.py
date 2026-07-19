class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        result = 0
        n = len(mat)

        if n % 2 != 0:
            for i in range(n):
                result += mat[i][i]
            for i in range(n):
                if i != n//2:
                    result += mat[i][n-i-1]
        else:
            for i in range(n):
                result += mat[i][i]
            for i in range(n):
                result += mat[i][n-i-1]
        return result
