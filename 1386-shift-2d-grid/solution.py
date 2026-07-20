class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid) - 1
        n = len(grid[0]) - 1
        temp1 = grid[0][0]
        for repeat in range(k):
            temp1 = grid[m][n]
            for i in range(m,-1,-1):
                temp = grid[i-1][n]
                for j in range(n,-0,-1):
                    grid[i][j] = grid[i][j-1]
                grid[i][0] = temp
            grid[0][0] = temp1
        return grid
