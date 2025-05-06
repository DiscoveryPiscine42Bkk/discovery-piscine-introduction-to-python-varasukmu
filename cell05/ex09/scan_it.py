#!/usr/bin/python3 

import re
import sys

# def main():
#     n = len(sys.argv)
#     if n < 3 :
#         print("none n")
#     else :
#         keyW = sys.argv[1]
#         txt = sys.argv[2]

#         try :
#             x = re.search(keyW, txt)
#             print(x.span()[1] - 1)
#         except :
#             print("none")

# main()


def main():
    try :
        keyW = sys.argv[1]
        txt = sys.argv[2]
        x = re.search(keyW, txt)
        print(x.span()[1] - 1)
    except :
        print("none")

main()
