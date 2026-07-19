class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        for i in range(n):
            s = set()
            for j in range(n):
                if matrix[i][j] != ".":
                    if matrix[i][j] not in s:
                        s.add(matrix[i][j])
                    else:
                        return False
        for i in range(n):
            s = set()
            for j in range(n):
                if matrix[j][i] != ".":
                    if matrix[j][i] not in s:
                        s.add(matrix[j][i])
                    else:
                        return False
        return True
