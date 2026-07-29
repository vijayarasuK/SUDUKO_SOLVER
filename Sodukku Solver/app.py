from flask import Flask, render_template, request

app = Flask(__name__)

# ===== STORE HISTORY =====
history = []

# ===== CHECK SAFE =====
def is_safe(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# ===== VALIDATE BOARD =====
def is_valid_board(board):
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != 0:
                board[r][c] = 0
                if not is_safe(board, r, c, num):
                    board[r][c] = num
                    return False
                board[r][c] = num
    return True

# ===== SOLVE =====
def solve_sudoku(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for num in range(1, 10):
                    if is_safe(board, r, c, num):
                        board[r][c] = num
                        if solve_sudoku(board):
                            return True
                        board[r][c] = 0
                return False
    return True

# ===== INTRO =====
@app.route('/')
def intro():
    return render_template('intro.html')

# ===== MAIN PAGE =====
@app.route('/home', methods=['GET', 'POST'])
def home():
    grid = [[0]*9 for _ in range(9)]
    error = None
    success = None

    if request.method == 'POST':
        grid = []

        for i in range(9):
            row = []
            for j in range(9):
                val = request.form.get(f'cell-{i}-{j}')

                if val and val.isdigit() and 1 <= int(val) <= 9:
                    row.append(int(val))
                else:
                    row.append(0)

            grid.append(row)

        if not is_valid_board(grid):
            error = "❌ Invalid Sudoku!"
            return render_template('index.html', grid=grid, error=error)

        solved = [row[:] for row in grid]

        if solve_sudoku(solved):
            history.append(solved)
            success = "✅ Solved successfully!"
            return render_template('index.html', grid=solved, success=success)
        else:
            error = "❌ No solution exists!"
            return render_template('index.html', grid=grid, error=error)

    return render_template('index.html', grid=grid)

# ===== HISTORY =====
@app.route('/history')
def show_history():
    return render_template('history.html', history=history)

# ===== CLEAR =====
@app.route('/clear')
def clear():
    grid = [[0]*9 for _ in range(9)]
    return render_template('index.html', grid=grid)

# ===== RUN =====
if __name__ == '__main__':
    app.run(debug=True)