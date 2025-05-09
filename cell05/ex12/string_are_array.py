#!/usr/bin/python3 

import sys

def main() :
    n = len(sys.argv)
    if n == 1 :
        print("none")
    else :
        cou = 0
        cou += sys.argv[1].count("z")

        # for i in sys.argv[1] :
        #     if i == "z" :
        #         cou += 1

        if not cou :
            print("none")
        else :
            print("z" * cou)
main()

