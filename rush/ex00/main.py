#!/usr/bin/env python3

from checkmate import checkboard, checkmate
# from checkmate import Pos_K

def main():
    board = """\
.......
.......
..B...P
..B....
..B..Q.
....K..
.......\
    """
    if checkboard(board) :
        checkmate(board)

if __name__ == "__main__":
    main()
