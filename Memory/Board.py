from game.symbol import make_symbols

def create_board(rows, cols):
    symbols = make_symbols(rows * cols // 2)
    board = []
    visible = []
    index = 0
    for r in range(rows):
        row = []
        vis_row = []
        for c in range(cols):
            row.append(symbols[index])
            vis_row.append(False)
            index += 1
        board.append(row)
        visible.append(vis_row)
    return board, visible





def print_board(board, visible):
    print()
    for r in range(len(board)):
        for c in range(len(board[0])):
            if visible [r][c]:
                print(board[r][c], end=" ")
            else:
                print("X", end=" ")
        print()
    print()




def reveal_card(visible, r, c):
    visible[r][c]=True



def hide_card(visible, r, c):
    visible[r][c]=False



def all_revealed(visible):
    for r in visible:
        for v in r:
            if not v:
                return False
    return True
