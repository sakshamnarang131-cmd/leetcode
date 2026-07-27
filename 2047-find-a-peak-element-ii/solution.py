class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        for i in range(len(mat)):
            mat[i].append(-1)
        mat.append([-1]*len(mat[0]))
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j] > mat[i-1][j] and mat[i][j] > mat[i][j-1] and mat[i][j] > mat[i+1][j] and mat[i][j] > mat[i][j+1]:
                    return [i,j]
