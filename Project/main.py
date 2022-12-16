from minesweeper import Game
from board import Board
import sys

if len(sys.argv) != 2:
    raise Exception("Wrong number of arguments")
arg = int(sys.argv[1])
board = None

'''
match(arg):
    case 1:
        board = Board(9,9,10)
    case 2:
        board = Board(16,16,40)
    case 3:
        board = Board(16,30,99)
    case _:
        raise Exception("Invalid argument")
'''

if arg == 1:
    board = Board(9,9,10)
elif arg == 2:
    board = Board(16,16,40)
elif arg == 3:
    board = Board(16,30,99)
else:
    raise Exception("Invalid argument")

game = Game(board)
game.run()