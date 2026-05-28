def solve_n_queen(n):

    solutions = []
    rows = set()
    diag1 = set()   # row - col
    diag2 = set()   # row + col

    board = ["." * n for _ in range(n)]

    def place(col):

        # Base case
        if col == n:
            solutions.append(board.copy())
            return

        for row in range(n):

            # Check if queen can be placed
            if row in rows or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Place queen
            rows.add(row)
            diag1.add(row - col)
            diag2.add(row + col)

            board[row] = (board[row][:col] + "Q" + board[row][col + 1:])

            # Recursive call
            place(col + 1)

            # Backtrack
            rows.remove(row)
            diag1.remove(row - col)
            diag2.remove(row + col)

            board[row] = (board[row][:col] + "." + board[row][col + 1:])

    place(0)
    return solutions


# Example
ans = solve_n_queen(4)

for solution in ans:
    for row in solution:
        print(row)
    print()


# Time Complexity(n!)
# Space Complexity(n)

'''The number of valid solutions for the 8-Queens Problem is:
👑 Total Solutions
92
So:
There are 92 valid arrangements
where 8 queens can be placed on an 8×8 chessboard
such that no two queens attack each other.
🔍 Unique Solutions
Many of those are symmetric (rotations/reflections).
The number of unique solutions is:
12
Meaning:
12 fundamentally different patterns
Remaining are rotations/mirrors of these.'''
