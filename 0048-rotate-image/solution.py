class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        a = []
        n = len(matrix)
        for j in range (n):
            for i in range (n):
                a.append(matrix[n-1-i][j])
        k = 0
        for i in range(n):
            for j in range(len(matrix[0])):
                matrix[i][j] = a[k]
                k +=1
        return a
