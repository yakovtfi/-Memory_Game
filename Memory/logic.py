def get_choice(rows, cols, visible, message):
    while True:
        try:
            text = input(message)
            parts = text.split(",")
            r = int(parts[0])
            c = int(parts[1])
            if r >= 0 and r < rows and c >= 0 and c < cols and not visible[r][c]:
                return r, c
            else:
                print("Invalid position.")
        except:
            print("Please enter row and column like: 1,2")

def check_match(board, r1, c1, r2, c2):
    return board[r1][c1] == board[r2][c2]
