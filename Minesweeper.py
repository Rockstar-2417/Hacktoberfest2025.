import random

def create_board(size, mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mine_coords = random.sample(range(size*size), mines)
    for coord in mine_coords:
        row = coord // size
        col = coord % size
        board[row][col] = 'M'
    return board

def print_board(visible_board):
    size = len(visible_board)
    print("\n  " + " ".join(str(i) for i in range(size)))
    for idx, row in enumerate(visible_board):
        print(f"{idx} " + " ".join(row))
    print()

def count_adjacent_mines(board, row, col):
    size = len(board)
    count = 0
    for r in range(max(0,row-1), min(size,row+2)):
        for c in range(max(0,col-1), min(size,col+2)):
            if board[r][c] == 'M':
                count += 1
    return count

def reveal(board, visible, row, col):
    if visible[row][col] != ' ':
        return
    if board[row][col] == 'M':
        visible[row][col] = 'M'
        return
    count = count_adjacent_mines(board,row,col)
    visible[row][col] = str(count)
    if count == 0:
        size = len(board)
        for r in range(max(0,row-1), min(size,row+2)):
            for c in range(max(0,col-1), min(size,col+2)):
                if visible[r][c] == ' ':
                    reveal(board,visible,r,c)

def check_win(board, visible):
    size = len(board)
    for r in range(size):
        for c in range(size):
            if board[r][c] != 'M' and visible[r][c] == ' ':
                return False
    return True

def main():
    size = 5
    mines = 5
    board = create_board(size, mines)
    visible = [[' ']*size for _ in range(size)]
    print("Mini Minesweeper ⚡ CLI Game")
    while True:
        print_board(visible)
        inp = input("Enter row,col (or 'exit'): ")
        if inp.lower() == 'exit':
            print("Game exited.")
            break
        try:
            row, col = map(int, inp.split(','))
            if row<0 or row>=size or col<0 or col>=size:
                print("Invalid coordinates.")
                continue
        except:
            print("Invalid input format.")
            continue
        if board[row][col] == 'M':
            print_board([['M' if cell=='M' else ' ' for cell in r] for r in board])
            print("💥 BOOM! You hit a mine. Game Over!")
            break
        else:
            reveal(board, visible, row, col)
        if check_win(board, visible):
            print_board(visible)
            print("🎉 Congrats! You cleared all safe cells!")
            break

if __name__=="__main__":
    main()
