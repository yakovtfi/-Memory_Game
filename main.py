from Memory.Board import create_board, print_board, reveal_card, hide_card, all_revealed
from Memory.logic import get_choice, check_match
import time
from Pygame import Tkinter

def main():
    print("Welcome to Memory Game (2 Players)!")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if (rows * cols) % 2 != 0:
        print("Board must have an even number of cells.")
        return

    board, visible = create_board(rows, cols)

    player1_score = 0
    player2_score = 0
    current_player = 1
    steps = 0

    while not all_revealed(visible):
        print_board(board, visible)
        print("Turn:", steps + 1)
        print("Player", current_player, "turn")
        print("Score -> Player 1:", player1_score, "| Player 2:", player2_score)
        print()

        r1, c1 = get_choice(rows, cols, visible, "Enter first card (row,col): ")
        reveal_card(visible, r1, c1)
        print_board(board, visible)

        r2, c2 = get_choice(rows, cols, visible, "Enter second card (row,col): ")
        reveal_card(visible, r2, c2)
        print_board(board, visible)

        if check_match(board, r1, c1, r2, c2):
            print("Match! Player", current_player, "gets a point!")
            if current_player == 1:
                player1_score += 1
            else:
                player2_score += 1
            print()
        else:
            print("Not a match.")
            time.sleep(1)
            hide_card(visible, r1, c1)
            hide_card(visible, r2, c2)
            current_player = 2 if current_player == 1 else 1
            print()

        steps += 1

    print_board(board, visible)
    print("Game Over!")
    print("Total steps:", steps)
    print("Final Scores  Player 1:", player1_score, "| Player 2:", player2_score)

    if player1_score > player2_score:
        print(" Player 1 wins!")
    elif player2_score > player1_score:
        print(" Player 2 wins!")
    else:
        print(" It's a tie!")
if __name__ == "__main__":
    main()