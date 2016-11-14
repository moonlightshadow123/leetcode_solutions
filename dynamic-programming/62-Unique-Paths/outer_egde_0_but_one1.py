class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mat = [[0 for _ in range(m+1)] for _ in range(n+1)]
        mat[n-1][m] = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                mat[i][j] = mat[i][j+1] + mat[i+1][j]
        return mat[0][0]
