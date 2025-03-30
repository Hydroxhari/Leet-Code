class Solution(object):
    def solveNQueens(self, n):
        g = [['.'] * n for _ in range(n)]
        a = []  # Stores final solutions

        def is_valid(r, c, gr):
            # Check column
            for i in range(r):
                if gr[i][c] == 'Q':
                    return False
            
            # Check diagonals
            for i in range(r):
                diff = r - i
                if c - diff >= 0 and gr[i][c - diff] == 'Q':  # Top-left diagonal
                    return False
                if c + diff < n and gr[i][c + diff] == 'Q':  # Top-right diagonal
                    return False
            
            return True

        def backtrack(r):
            if r == n:
                # Convert board to string format
                a.append(["".join(row) for row in g])
                return
            
            for c in range(n):
                if is_valid(r, c, g):
                    g[r][c] = "Q"
                    backtrack(r + 1)
                    g[r][c] = '.'  # Backtrack

        backtrack(0)
        return a
