class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # 1. Pre-populate sets and collect all empty cells upfront
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(idx):
            # All empty cells have been filled
            if idx == len(empty):
                return True

            # 2. MRV Heuristic: Pick the empty cell with the fewest valid choices first
            best_idx = idx
            min_choices = 10
            for i in range(idx, len(empty)):
                r, c = empty[i]
                b = (r // 3) * 3 + (c // 3)
                choices = 9 - len(rows[r] | cols[c] | boxes[b])
                if choices < min_choices:
                    min_choices = choices
                    best_idx = i
                if min_choices <= 1:
                    break

            # Swap the most constrained cell into the current position
            empty[idx], empty[best_idx] = empty[best_idx], empty[idx]
            r, c = empty[idx]
            b = (r // 3) * 3 + (c // 3)

            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[b]:
                    # Choose
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

                    # Explore
                    if backtrack(idx + 1):
                        return True

                    # Backtrack
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[b].remove(num)

            # Restore swap order on backtrack
            empty[idx], empty[best_idx] = empty[best_idx], empty[idx]
            return False

        backtrack(0)
