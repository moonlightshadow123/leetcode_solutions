class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        elements = []
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = -1
        while True:
            for i in range(n):
                col += 1
                elements.append(matrix[row][col])
            m -= 1
            if m == 0:
                break
            #####################################
            for i in range(m):
                row += 1
                elements.append(matrix[row][col])
            n -= 1
            if n == 0:
                break
            ####################################
            for i in range(n):
                col -= 1
                elements.append(matrix[row][col])
            m -= 1
            if m == 0:
                break
            ####################################
            for i in range(m):
                row -= 1
                elements.append(matrix[row][col])
            n -= 1
            if n == 0:
                break
        return elements
