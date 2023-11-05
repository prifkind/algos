class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                # Swap element at (i, j) with element at (j, i)
                # This takes each row, and turns it into a column
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row to get the correct arrangement
        for i in range(n):
            matrix[i].reverse()
