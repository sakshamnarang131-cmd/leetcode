class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        result = 0
        for j in range(n):
            for i in range(1,m):
                if grid[i][j] <= grid[i-1][j]:
                    result += grid[i-1][j] +1 - grid[i][j]
                    grid[i][j] = grid[i-1][j] +1
        return result
