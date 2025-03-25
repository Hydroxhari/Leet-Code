class Solution(object):
    def exist(self, b, w):
        m, n = len(b), len(b[0])  # Dimensions of the board

        def backtrack(i, j, k):
            # Base case: If we've matched all characters in the word
            if k == len(w):
                return True

            # Boundary check and character mismatch check
            if i < 0 or i >= m or j < 0 or j >= n or b[i][j] != w[k]:
                return False

            # Save the current cell and mark it as visited
            temp = b[i][j]
            b[i][j] = '#'

            # Explore all 4 possible directions (right, left, down, up)
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if backtrack(i + x, j + y, k + 1):
                    return True

            # Backtrack: Restore the original character
            b[i][j] = temp
            return False

        # Start backtracking from each cell matching the first character
        for i in range(m):
            for j in range(n):
                if b[i][j] == w[0] and backtrack(i, j, 0):
                    return True

        return False