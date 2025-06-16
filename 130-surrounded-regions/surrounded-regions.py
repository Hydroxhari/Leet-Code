class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = '#'
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                dfs(i+x, j+y)

        # Step 1: Mark safe 'O's from border
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        # Step 2: Flip all 'O' to 'X', and '#' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'

        return board
