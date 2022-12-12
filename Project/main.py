from minesweeper import Game
from board import Board

board = Board(16,16,40)
game = Game(board)
game.run()

# TODO : win / loss logic , timer , maybe changeable board