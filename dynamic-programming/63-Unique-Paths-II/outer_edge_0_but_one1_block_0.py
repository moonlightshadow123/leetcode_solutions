class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mat = [[0 for _ in range(n+1)] for _ in range(m+1)]
        mat[m-1][n] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    mat[i][j] = 0
                else:
                    mat[i][j] = mat[i+1][j] + mat[i][j+1]
        return mat[0][0]
