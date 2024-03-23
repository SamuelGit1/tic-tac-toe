from board import Board
from player import Player

board = Board()
player1 = Player("Player1", "X", board)
player2 = Player("Player2", "O", board)
current_player = player1
next_player = player2

while True:
    board.draw()
    winner = board.check_winner()

    if player1.piece == winner:
        print("Player 1 Wins!")
        break
    elif player2.piece == winner:
        print("Player 2 Wins!")
        break
    elif board.is_full():
        print("Tie!")
        break

    is_valid = current_player.get_input()
    if is_valid:
        current_player, next_player = next_player, current_player
    else:
        print("invalid input")
