class Solution(object):
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        res = []
        i, j = 0, 0
        direction = 1   # 1 = up-right, -1 = down-left
        
        for _ in range(m * n):
            res.append(mat[i][j])
            
            if direction == 1:  # moving up-right
                if j == n - 1:   # hit right border
                    i += 1
                    direction = -1
                elif i == 0:     # hit top border
                    j += 1
                    direction = -1
                else:
                    i -= 1
                    j += 1
            else:  # moving down-left
                if i == m - 1:   # hit bottom border
                    j += 1
                    direction = 1
                elif j == 0:     # hit left border
                    i += 1
                    direction = 1
                else:
                    i += 1
                    j -= 1
                    
        return res
