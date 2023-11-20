class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows_to_update = set()
        columns_to_update = set()

        # Loop through the matrix and find the rows and columns that need to be set to zeroes
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == 0:
                    rows_to_update.add(i)
                    columns_to_update.add(j)

        # Set the identified rows to zeroes
        for i in rows_to_update:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        # Set the identified columns to zeroes
        for j in columns_to_update:
            for i in range(len(matrix)):
                matrix[i][j] = 0

        # The function returns None as it modifies the matrix in-place


