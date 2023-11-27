class Solution:
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            ''' Depth-first search from board[r][c] for word[i:]. '''
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                board[r][c] == "#"):  # Marked as part of the path
                return False

            # Mark the choice before exploring further.
            temp, board[r][c] = board[r][c], '#'
            # Explore the four possible directions.
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            # Unmark the choice, backtracking.
            board[r][c] = temp
            return res

        # Check every position on the board for the start of the word.
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
