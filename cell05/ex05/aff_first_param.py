#!/usr/bin/python3 

import sys

def main():
    try :
        print(sys.argv[1])
    except :
        print("none")
main()


# import sys

# def main():
#     n = len(sys.argv) - 1
#     if n > 1 :
#         print(sys.argv[1])
#     else :
#         print("none")
# main()