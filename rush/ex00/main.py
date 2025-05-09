#!/usr/bin/env python3

from checkmate import checkboard, checkmate
# from checkmate import Pos_K

def main():
    board = """\
.......
.......
.......
P......
..Q....
.....Q.
.......\
    """
    if checkboard(board) :
        checkmate(board)

if __name__ == "__main__":
    main()
