class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        mat = [[0] * n for _ in range(m)]
        for i, j in walls:
            mat[i][j] = 2  # wall
        for i, j in guards:
            mat[i][j] = 3  # guard

        # directions: (up, down, left, right)
        # We’ll sweep line by line for guards’ vision
        for i in range(m):
            seen = False
            for j in range(n):
                if mat[i][j] == 2: seen = False
                elif mat[i][j] == 3: seen = True
                elif seen: mat[i][j] = 1  # guarded
            seen = False
            for j in range(n-1, -1, -1):
                if mat[i][j] == 2: seen = False
                elif mat[i][j] == 3: seen = True
                elif seen: mat[i][j] = 1

        for j in range(n):
            seen = False
            for i in range(m):
                if mat[i][j] == 2: seen = False
                elif mat[i][j] == 3: seen = True
                elif seen: mat[i][j] = 1
            seen = False
            for i in range(m-1, -1, -1):
                if mat[i][j] == 2: seen = False
                elif mat[i][j] == 3: seen = True
                elif seen: mat[i][j] = 1

        # Count unguarded
        c = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    c += 1
        return c
