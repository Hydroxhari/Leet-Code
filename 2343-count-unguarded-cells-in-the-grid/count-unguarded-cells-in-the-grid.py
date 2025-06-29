class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        wall_set = set(map(tuple, walls))
        guard_set = set(map(tuple, guards))
        seen = set()
        
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for x, y in guards:
            for dx, dy in DIRS:
                i, j = x + dx, y + dy
                while 0 <= i < m and 0 <= j < n:
                    if (i, j) in wall_set or (i, j) in guard_set:
                        break
                    if (i, j) not in seen:
                        seen.add((i, j))
                    i += dx
                    j += dy
        
        total_cells = m * n
        unguarded = total_cells - len(seen) - len(wall_set) - len(guard_set)
        return unguarded
