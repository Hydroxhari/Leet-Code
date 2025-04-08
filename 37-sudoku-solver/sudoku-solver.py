class Solution(object):
    def solveSudoku(self, board):
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        empty_cells = []
        
        # Preprocess the board
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))  # Store empty cell positions
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)

        def backtrack(index):
            if index == len(empty_cells):
                return True  # Board solved

            r, c = empty_cells[index]  # Get next empty cell
            box_index = (r // 3) * 3 + (c // 3)

            for num in map(str, range(1, 10)):  # Try numbers '1' to '9'
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

                    if backtrack(index + 1):  # Recursively solve next empty cell
                        return True  # Stop if solution is found

                    # Undo move (backtrack)
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_index].remove(num)

            return False  # No valid number found, backtrack

        backtrack(0)
